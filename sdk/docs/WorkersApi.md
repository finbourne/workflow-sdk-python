# lusid_workflow.WorkersApi

All URIs are relative to *https://fbn-prd.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_worker**](WorkersApi.md#create_worker) | **POST** /api/workers | [EXPERIMENTAL] CreateWorker: Create a new Worker
[**delete_worker**](WorkersApi.md#delete_worker) | **DELETE** /api/workers/{scope}/{code} | [EXPERIMENTAL] DeleteWorker: Delete a Worker
[**get_worker**](WorkersApi.md#get_worker) | **GET** /api/workers/{scope}/{code} | [EXPERIMENTAL] GetWorker: Get a Worker
[**get_worker_result**](WorkersApi.md#get_worker_result) | **GET** /api/workers/{runId}/$result | [EXPERIMENTAL] GetWorkerResult: Get the status of a specific run of a worker with any relevant results
[**list_workers**](WorkersApi.md#list_workers) | **GET** /api/workers | [EXPERIMENTAL] ListWorkers: List Workers
[**run_worker**](WorkersApi.md#run_worker) | **POST** /api/workers/{scope}/{code}/$run | [EXPERIMENTAL] RunWorker: Run a Worker
[**update_worker**](WorkersApi.md#update_worker) | **PUT** /api/workers/{scope}/{code} | [EXPERIMENTAL] UpdateWorker: Update a Worker


# **create_worker**
> Worker create_worker(create_worker_request)

[EXPERIMENTAL] CreateWorker: Create a new Worker

If the Worker already exists a failure will be returned

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    WorkersApi
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
    api_instance = api_client_factory.build(WorkersApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_worker_request = CreateWorkerRequest.from_json("")
    # create_worker_request = CreateWorkerRequest.from_dict({})
    create_worker_request = CreateWorkerRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_worker(create_worker_request, opts=opts)

        # [EXPERIMENTAL] CreateWorker: Create a new Worker
        api_response = api_instance.create_worker(create_worker_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkersApi->create_worker: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_worker_request** | [**CreateWorkerRequest**](CreateWorkerRequest.md)| Worker to be created | 

### Return type

[**Worker**](Worker.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_worker**
> DeletedEntityResponse delete_worker(scope, code)

[EXPERIMENTAL] DeleteWorker: Delete a Worker

If the Worker does not exist a failure will be returned

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    WorkersApi
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
    api_instance = api_client_factory.build(WorkersApi)
    scope = 'scope_example' # str | Scope of the worker to be deleted
    code = 'code_example' # str | Code of the worker to be deleted

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_worker(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteWorker: Delete a Worker
        api_response = api_instance.delete_worker(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkersApi->delete_worker: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the worker to be deleted | 
 **code** | **str**| Code of the worker to be deleted | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | Worker not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_worker**
> Worker get_worker(scope, code, as_at=as_at)

[EXPERIMENTAL] GetWorker: Get a Worker

Will return a NotFound failure if the Worker does not exist

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    WorkersApi
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
    api_instance = api_client_factory.build(WorkersApi)
    scope = 'scope_example' # str | Scope of the worker
    code = 'code_example' # str | Code of the worker
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Worker. Defaults to returning the latest version of the Worker if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_worker(scope, code, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetWorker: Get a Worker
        api_response = api_instance.get_worker(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkersApi->get_worker: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the worker | 
 **code** | **str**| Code of the worker | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Worker. Defaults to returning the latest version of the Worker if not specified. | [optional] 

### Return type

[**Worker**](Worker.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_worker_result**
> GetWorkerResultResponse get_worker_result(run_id)

[EXPERIMENTAL] GetWorkerResult: Get the status of a specific run of a worker with any relevant results

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    WorkersApi
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
    api_instance = api_client_factory.build(WorkersApi)
    run_id = 'run_id_example' # str | The ID returned when calling Run Worker

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_worker_result(run_id, opts=opts)

        # [EXPERIMENTAL] GetWorkerResult: Get the status of a specific run of a worker with any relevant results
        api_response = api_instance.get_worker_result(run_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkersApi->get_worker_result: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The ID returned when calling Run Worker | 

### Return type

[**GetWorkerResultResponse**](GetWorkerResultResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_workers**
> PagedResourceListOfWorker list_workers(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)

[EXPERIMENTAL] ListWorkers: List Workers

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    WorkersApi
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
    api_instance = api_client_factory.build(WorkersApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Workers. Defaults to return the latest version of each Worker if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each optionally suffixed by \" ASC\" or \" DESC\" (optional)
    limit = 10 # int | When paginating, limit the number of returned results to this many. (optional) (default to 10)
    page = 'page_example' # str | The pagination token to use to continue listing workers from a previous call to list workers. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_workers(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page, opts=opts)

        # [EXPERIMENTAL] ListWorkers: List Workers
        api_response = api_instance.list_workers(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkersApi->list_workers: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Workers. Defaults to return the latest version of each Worker if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each optionally suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing workers from a previous call to list workers. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfWorker**](PagedResourceListOfWorker.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **run_worker**
> RunWorkerResponse run_worker(scope, code, run_worker_request, as_at=as_at)

[EXPERIMENTAL] RunWorker: Run a Worker

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    WorkersApi
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
    api_instance = api_client_factory.build(WorkersApi)
    scope = 'scope_example' # str | Scope of the worker
    code = 'code_example' # str | Code of the worker

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # run_worker_request = RunWorkerRequest.from_json("")
    # run_worker_request = RunWorkerRequest.from_dict({})
    run_worker_request = RunWorkerRequest()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Worker. Defaults to returning the latest version of the Worker if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.run_worker(scope, code, run_worker_request, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] RunWorker: Run a Worker
        api_response = api_instance.run_worker(scope, code, run_worker_request, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkersApi->run_worker: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the worker | 
 **code** | **str**| Code of the worker | 
 **run_worker_request** | [**RunWorkerRequest**](RunWorkerRequest.md)|  | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Worker. Defaults to returning the latest version of the Worker if not specified. | [optional] 

### Return type

[**RunWorkerResponse**](RunWorkerResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_worker**
> Worker update_worker(scope, code, update_worker_request)

[EXPERIMENTAL] UpdateWorker: Update a Worker

If the Worker does not exist a failure will be returned

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    WorkersApi
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
    api_instance = api_client_factory.build(WorkersApi)
    scope = 'scope_example' # str | Scope of the worker to be updated
    code = 'code_example' # str | Code of the worker to be updated

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_worker_request = UpdateWorkerRequest.from_json("")
    # update_worker_request = UpdateWorkerRequest.from_dict({})
    update_worker_request = UpdateWorkerRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_worker(scope, code, update_worker_request, opts=opts)

        # [EXPERIMENTAL] UpdateWorker: Update a Worker
        api_response = api_instance.update_worker(scope, code, update_worker_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkersApi->update_worker: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the worker to be updated | 
 **code** | **str**| Code of the worker to be updated | 
 **update_worker_request** | [**UpdateWorkerRequest**](UpdateWorkerRequest.md)| State of the updated worker | 

### Return type

[**Worker**](Worker.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | Worker not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

