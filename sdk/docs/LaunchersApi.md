# lusid_workflow.LaunchersApi

All URIs are relative to *https://fbn-prd.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_launcher**](LaunchersApi.md#create_launcher) | **POST** /api/workflows/{scope}/{code}/launchers | [EXPERIMENTAL] CreateLauncher: Create a new Launcher on a Workflow
[**delete_launcher**](LaunchersApi.md#delete_launcher) | **DELETE** /api/workflows/{scope}/{code}/launchers/{launcherId} | [EXPERIMENTAL] DeleteLauncher: Delete a Launcher of a Workflow
[**get_launcher**](LaunchersApi.md#get_launcher) | **GET** /api/workflows/{scope}/{code}/launchers/{launcherId} | [EXPERIMENTAL] GetLauncher: Get a Launcher of a Workflow
[**list_launchers**](LaunchersApi.md#list_launchers) | **GET** /api/workflows/{scope}/{code}/launchers | [EXPERIMENTAL] ListLaunchers: List the Launchers of a Workflow
[**update_launcher**](LaunchersApi.md#update_launcher) | **PUT** /api/workflows/{scope}/{code}/launchers/{launcherId} | [EXPERIMENTAL] UpdateLauncher: Update an existing Launcher of a Workflow


# **create_launcher**
> LauncherResponse create_launcher(scope, code, create_launcher_request)

[EXPERIMENTAL] CreateLauncher: Create a new Launcher on a Workflow

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    LaunchersApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "workflowUrl":"https://<your-domain>.lusid.com/workflow",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_workflow SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(LaunchersApi)
    scope = 'scope_example' # str | The scope that identifies the Workflow that owns the Launcher
    code = 'code_example' # str | The code that identifies the Workflow that owns the Launcher

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_launcher_request = CreateLauncherRequest.from_json("")
    # create_launcher_request = CreateLauncherRequest.from_dict({})
    create_launcher_request = CreateLauncherRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_launcher(scope, code, create_launcher_request, opts=opts)

        # [EXPERIMENTAL] CreateLauncher: Create a new Launcher on a Workflow
        api_response = api_instance.create_launcher(scope, code, create_launcher_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LaunchersApi->create_launcher: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies the Workflow that owns the Launcher | 
 **code** | **str**| The code that identifies the Workflow that owns the Launcher | 
 **create_launcher_request** | [**CreateLauncherRequest**](CreateLauncherRequest.md)| The data to create a Launcher | 

### Return type

[**LauncherResponse**](LauncherResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**404** | Workflow not found. |  -  |
**409** | Launcher already exists. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_launcher**
> DeletedEntityResponse delete_launcher(scope, code, launcher_id)

[EXPERIMENTAL] DeleteLauncher: Delete a Launcher of a Workflow

If the Launcher does not exist a failure will be returned

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    LaunchersApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "workflowUrl":"https://<your-domain>.lusid.com/workflow",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_workflow SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(LaunchersApi)
    scope = 'scope_example' # str | The scope that identifies the Workflow that owns the Launcher
    code = 'code_example' # str | The code that identifies the Workflow that owns the Launcher
    launcher_id = 'launcher_id_example' # str | The identifier of the Launcher inside its Workflow

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_launcher(scope, code, launcher_id, opts=opts)

        # [EXPERIMENTAL] DeleteLauncher: Delete a Launcher of a Workflow
        api_response = api_instance.delete_launcher(scope, code, launcher_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LaunchersApi->delete_launcher: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies the Workflow that owns the Launcher | 
 **code** | **str**| The code that identifies the Workflow that owns the Launcher | 
 **launcher_id** | **str**| The identifier of the Launcher inside its Workflow | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Launcher not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_launcher**
> LauncherResponse get_launcher(scope, code, launcher_id, as_at=as_at)

[EXPERIMENTAL] GetLauncher: Get a Launcher of a Workflow

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    LaunchersApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "workflowUrl":"https://<your-domain>.lusid.com/workflow",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_workflow SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(LaunchersApi)
    scope = 'scope_example' # str | The scope that identifies the Workflow that owns the Launcher
    code = 'code_example' # str | The code that identifies the Workflow that owns the Launcher
    launcher_id = 'launcher_id_example' # str | The identifier of the Launcher inside its Workflow
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Launcher. Defaults to returning the latest             version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_launcher(scope, code, launcher_id, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetLauncher: Get a Launcher of a Workflow
        api_response = api_instance.get_launcher(scope, code, launcher_id, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LaunchersApi->get_launcher: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies the Workflow that owns the Launcher | 
 **code** | **str**| The code that identifies the Workflow that owns the Launcher | 
 **launcher_id** | **str**| The identifier of the Launcher inside its Workflow | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Launcher. Defaults to returning the latest             version if not specified. | [optional] 

### Return type

[**LauncherResponse**](LauncherResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Launcher not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_launchers**
> PagedResourceListOfLauncherResponse list_launchers(scope, code, as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)

[EXPERIMENTAL] ListLaunchers: List the Launchers of a Workflow

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    LaunchersApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "workflowUrl":"https://<your-domain>.lusid.com/workflow",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_workflow SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(LaunchersApi)
    scope = 'scope_example' # str | The scope that identifies the Workflow that owns the Launchers
    code = 'code_example' # str | The code that identifies the Workflow that owns the Launchers
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Launchers. Defaults to return the latest version             of each Launcher if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:             https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". Defaults to             \"launcherId ASC\" if not specified. (optional)
    limit = 10 # int | When paginating, limit the number of returned results to this many. (optional) (default to 10)
    page = 'page_example' # str | The pagination token to use to continue listing Launchers from a previous call to list             Launchers. This value is returned from the previous call. If a pagination token is provided the sortBy,             filter, and asAt fields must not have changed since the original request. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_launchers(scope, code, as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page, opts=opts)

        # [EXPERIMENTAL] ListLaunchers: List the Launchers of a Workflow
        api_response = api_instance.list_launchers(scope, code, as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LaunchersApi->list_launchers: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies the Workflow that owns the Launchers | 
 **code** | **str**| The code that identifies the Workflow that owns the Launchers | 
 **as_at** | **datetime**| The asAt datetime at which to list the Launchers. Defaults to return the latest version             of each Launcher if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:             https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. Defaults to             \&quot;launcherId ASC\&quot; if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing Launchers from a previous call to list             Launchers. This value is returned from the previous call. If a pagination token is provided the sortBy,             filter, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfLauncherResponse**](PagedResourceListOfLauncherResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Workflow not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_launcher**
> LauncherResponse update_launcher(scope, code, launcher_id, update_launcher_request)

[EXPERIMENTAL] UpdateLauncher: Update an existing Launcher of a Workflow

The type of a Launcher cannot be changed

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    LaunchersApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "workflowUrl":"https://<your-domain>.lusid.com/workflow",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_workflow SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(LaunchersApi)
    scope = 'scope_example' # str | The scope that identifies the Workflow that owns the Launcher
    code = 'code_example' # str | The code that identifies the Workflow that owns the Launcher
    launcher_id = 'launcher_id_example' # str | The identifier of the Launcher inside its Workflow

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_launcher_request = UpdateLauncherRequest.from_json("")
    # update_launcher_request = UpdateLauncherRequest.from_dict({})
    update_launcher_request = UpdateLauncherRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_launcher(scope, code, launcher_id, update_launcher_request, opts=opts)

        # [EXPERIMENTAL] UpdateLauncher: Update an existing Launcher of a Workflow
        api_response = api_instance.update_launcher(scope, code, launcher_id, update_launcher_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LaunchersApi->update_launcher: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies the Workflow that owns the Launcher | 
 **code** | **str**| The code that identifies the Workflow that owns the Launcher | 
 **launcher_id** | **str**| The identifier of the Launcher inside its Workflow | 
 **update_launcher_request** | [**UpdateLauncherRequest**](UpdateLauncherRequest.md)| The data to update a Launcher | 

### Return type

[**LauncherResponse**](LauncherResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Launcher not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

