# lusid_workflow.WorkflowsApi

All URIs are relative to *https://fbn-prd.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow**](WorkflowsApi.md#create_workflow) | **POST** /api/workflows | CreateWorkflow: Create a new Workflow
[**delete_workflow**](WorkflowsApi.md#delete_workflow) | **DELETE** /api/workflows/{scope}/{code} | [EXPERIMENTAL] DeleteWorkflow: Delete a Workflow
[**get_workflow**](WorkflowsApi.md#get_workflow) | **GET** /api/workflows/{scope}/{code} | GetWorkflow: Get a Workflow
[**list_workflows**](WorkflowsApi.md#list_workflows) | **GET** /api/workflows | ListWorkflows: List Workflows


# **create_workflow**
> WorkflowResponse create_workflow(create_workflow_request)

CreateWorkflow: Create a new Workflow

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    WorkflowsApi
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
    api_instance = api_client_factory.build(WorkflowsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_workflow_request = CreateWorkflowRequest.from_json("")
    # create_workflow_request = CreateWorkflowRequest.from_dict({})
    create_workflow_request = CreateWorkflowRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_workflow(create_workflow_request, opts=opts)

        # CreateWorkflow: Create a new Workflow
        api_response = api_instance.create_workflow(create_workflow_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workflow_request** | [**CreateWorkflowRequest**](CreateWorkflowRequest.md)| The data to create a Workflow | 

### Return type

[**WorkflowResponse**](WorkflowResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**409** | Workflow already exists. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_workflow**
> DeletedEntityResponse delete_workflow(scope, code)

[EXPERIMENTAL] DeleteWorkflow: Delete a Workflow

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    WorkflowsApi
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
    api_instance = api_client_factory.build(WorkflowsApi)
    scope = 'scope_example' # str | The scope that identifies a Workflow
    code = 'code_example' # str | The code that identifies a Workflow

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_workflow(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteWorkflow: Delete a Workflow
        api_response = api_instance.delete_workflow(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkflowsApi->delete_workflow: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Workflow | 
 **code** | **str**| The code that identifies a Workflow | 

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
**404** | Workflow not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_workflow**
> WorkflowResponse get_workflow(scope, code, as_at=as_at)

GetWorkflow: Get a Workflow

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    WorkflowsApi
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
    api_instance = api_client_factory.build(WorkflowsApi)
    scope = 'scope_example' # str | The scope that identifies a Workflow
    code = 'code_example' # str | The code that identifies a Workflow
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Workflow. Defaults to returning the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_workflow(scope, code, as_at=as_at, opts=opts)

        # GetWorkflow: Get a Workflow
        api_response = api_instance.get_workflow(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflow: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Workflow | 
 **code** | **str**| The code that identifies a Workflow | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Workflow. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**WorkflowResponse**](WorkflowResponse.md)

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

# **list_workflows**
> PagedResourceListOfWorkflowResponse list_workflows(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)

ListWorkflows: List Workflows

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    WorkflowsApi
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
    api_instance = api_client_factory.build(WorkflowsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Workflows. Defaults to return the latest version of each Workflow if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    limit = 10 # int | When paginating, limit the number of returned results to this many. (optional) (default to 10)
    page = 'page_example' # str | The pagination token to use to continue listing workflows from a previous call to list workflows. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_workflows(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page, opts=opts)

        # ListWorkflows: List Workflows
        api_response = api_instance.list_workflows(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkflowsApi->list_workflows: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Workflows. Defaults to return the latest version of each Workflow if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing workflows from a previous call to list workflows. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfWorkflowResponse**](PagedResourceListOfWorkflowResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No Workflows found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

