# lusid_workflow.TasksApi

All URIs are relative to *https://fbn-prd.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](TasksApi.md#create_task) | **POST** /api/tasks | [EXPERIMENTAL] CreateTask: Create a new Task
[**delete_task**](TasksApi.md#delete_task) | **DELETE** /api/tasks/{id} | [EXPERIMENTAL] DeleteTask: Delete a Task
[**get_task**](TasksApi.md#get_task) | **GET** /api/tasks/{id} | [EXPERIMENTAL] GetTask: Get a Task
[**get_task_history**](TasksApi.md#get_task_history) | **GET** /api/tasks/{id}/history | [EXPERIMENTAL] GetTaskHistory: Get the history of a Task
[**list_tasks**](TasksApi.md#list_tasks) | **GET** /api/tasks | ListTasks: List Tasks
[**update_task**](TasksApi.md#update_task) | **POST** /api/tasks/{id} | [EXPERIMENTAL] UpdateTask: Update a Task


# **create_task**
> Task create_task(create_task_request, trigger=trigger)

[EXPERIMENTAL] CreateTask: Create a new Task

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    TasksApi
)

async def main():

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

    # Use the lusid_workflow ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TasksApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_task_request = CreateTaskRequest.from_json("")
        # create_task_request = CreateTaskRequest.from_dict({})
        create_task_request = CreateTaskRequest()
        trigger = 'trigger_example' # str | The name of the Trigger to invoke (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.create_task(create_task_request, trigger=trigger, opts=opts)

            # [EXPERIMENTAL] CreateTask: Create a new Task
            api_response = await api_instance.create_task(create_task_request, trigger=trigger)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TasksApi->create_task: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_task_request** | [**CreateTaskRequest**](CreateTaskRequest.md)| Request to create Task | 
 **trigger** | **str**| The name of the Trigger to invoke | [optional] 

### Return type

[**Task**](Task.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_task**
> DeletedEntityResponse delete_task(id)

[EXPERIMENTAL] DeleteTask: Delete a Task

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    TasksApi
)

async def main():

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

    # Use the lusid_workflow ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TasksApi)
        id = 'id_example' # str | The identifier for the Task to be deleted.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.delete_task(id, opts=opts)

            # [EXPERIMENTAL] DeleteTask: Delete a Task
            api_response = await api_instance.delete_task(id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TasksApi->delete_task: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier for the Task to be deleted. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | Task not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_task**
> Task get_task(id, as_at=as_at)

[EXPERIMENTAL] GetTask: Get a Task

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    TasksApi
)

async def main():

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

    # Use the lusid_workflow ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TasksApi)
        id = 'id_example' # str | Id of the Task to retrieve
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Task. Defaults to returning the latest version of the Task if not specified. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_task(id, as_at=as_at, opts=opts)

            # [EXPERIMENTAL] GetTask: Get a Task
            api_response = await api_instance.get_task(id, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TasksApi->get_task: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Task to retrieve | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Task. Defaults to returning the latest version of the Task if not specified. | [optional] 

### Return type

[**Task**](Task.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | Task not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_task_history**
> ResourceListOfChangeItem get_task_history(id, as_at=as_at)

[EXPERIMENTAL] GetTaskHistory: Get the history of a Task

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    TasksApi
)

async def main():

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

    # Use the lusid_workflow ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TasksApi)
        id = 'id_example' # str | The Task Id for which to get the history
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime of the oldest change to retrieve. Defaults to returning the latest version of the Task if not specified. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_task_history(id, as_at=as_at, opts=opts)

            # [EXPERIMENTAL] GetTaskHistory: Get the history of a Task
            api_response = await api_instance.get_task_history(id, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TasksApi->get_task_history: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Task Id for which to get the history | 
 **as_at** | **datetime**| The asAt datetime of the oldest change to retrieve. Defaults to returning the latest version of the Task if not specified. | [optional] 

### Return type

[**ResourceListOfChangeItem**](ResourceListOfChangeItem.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | Task not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_tasks**
> PagedResourceListOfTask list_tasks(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)

ListTasks: List Tasks

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    TasksApi
)

async def main():

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

    # Use the lusid_workflow ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TasksApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Tasks. Defaults to return the latest version of each Task if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each optionally suffixed by \" ASC\" or \" DESC\" (optional)
        limit = 10 # int | When paginating, limit the number of returned results to this many. (optional) (default to 10)
        page = 'page_example' # str | The pagination token to use to continue listing tasks from a previous call to list tasks. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_tasks(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page, opts=opts)

            # ListTasks: List Tasks
            api_response = await api_instance.list_tasks(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TasksApi->list_tasks: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Tasks. Defaults to return the latest version of each Task if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each optionally suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing tasks from a previous call to list tasks. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfTask**](PagedResourceListOfTask.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No Tasks found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_task**
> Task update_task(id, trigger=trigger, update_task_request=update_task_request)

[EXPERIMENTAL] UpdateTask: Update a Task

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    TasksApi
)

async def main():

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

    # Use the lusid_workflow ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TasksApi)
        id = 'id_example' # str | Id of the Task to act upon
        trigger = 'trigger_example' # str |  (optional)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_task_request = UpdateTaskRequest.from_json("")
        # update_task_request = UpdateTaskRequest.from_dict({})
        update_task_request = UpdateTaskRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.update_task(id, trigger=trigger, update_task_request=update_task_request, opts=opts)

            # [EXPERIMENTAL] UpdateTask: Update a Task
            api_response = await api_instance.update_task(id, trigger=trigger, update_task_request=update_task_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TasksApi->update_task: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Task to act upon | 
 **trigger** | **str**|  | [optional] 
 **update_task_request** | [**UpdateTaskRequest**](UpdateTaskRequest.md)| The details of the request | [optional] 

### Return type

[**Task**](Task.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | Task not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

