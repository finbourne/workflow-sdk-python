# lusid_workflow.TaskDefinitionsApi

All URIs are relative to *https://fbn-prd.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_definition**](TaskDefinitionsApi.md#create_task_definition) | **POST** /api/taskdefinitions | [EXPERIMENTAL] CreateTaskDefinition: Create a new Task Definition
[**delete_task_definition**](TaskDefinitionsApi.md#delete_task_definition) | **DELETE** /api/taskdefinitions/{scope}/{code} | [EXPERIMENTAL] DeleteTaskDefinition: Delete a Task Definition
[**get_task_definition**](TaskDefinitionsApi.md#get_task_definition) | **GET** /api/taskdefinitions/{scope}/{code} | [EXPERIMENTAL] GetTaskDefinition: Get a Task Definition
[**list_task_definitions**](TaskDefinitionsApi.md#list_task_definitions) | **GET** /api/taskdefinitions | [EXPERIMENTAL] ListTaskDefinitions: List Task Definitions
[**list_tasks_for_task_definition**](TaskDefinitionsApi.md#list_tasks_for_task_definition) | **GET** /api/taskdefinitions/{scope}/{code}/tasks | [EXPERIMENTAL] ListTasksForTaskDefinition: List Tasks for a Task Definition
[**update_task_definition**](TaskDefinitionsApi.md#update_task_definition) | **PUT** /api/taskdefinitions/{scope}/{code} | [EXPERIMENTAL] UpdateTaskDefinition: Update an existing Task Definition


# **create_task_definition**
> TaskDefinition create_task_definition(create_task_definition_request)

[EXPERIMENTAL] CreateTaskDefinition: Create a new Task Definition

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    TaskDefinitionsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TaskDefinitionsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_task_definition_request = CreateTaskDefinitionRequest()
        # create_task_definition_request = CreateTaskDefinitionRequest.from_json("")
        create_task_definition_request = CreateTaskDefinitionRequest.from_dict({"id":{"scope":"A1","code":"ZZZ"},"displayName":"An example TaskDefinition","description":"Test","states":[{"name":"Submitted"},{"name":"InProgress"},{"name":"SendingSurvey"},{"name":"Done"},{"name":"SurveyNotSent"},{"name":"NotDone"}],"fieldSchema":[{"name":"clientId","type":"String"},{"name":"assignee","type":"String","readOnlyStates":{"stateType":"SelectedStates","selectedStates":["Submitted","Done","SurveyNotSent","NotDone"]}},{"name":"resolutionDetail","type":"String","readOnlyStates":{"stateType":"TerminalState"}}],"initialState":{"name":"Submitted","requiredFields":["clientId"]},"triggers":[{"name":"start","trigger":{"type":"External"}},{"name":"cancel","trigger":{"type":"External"}},{"name":"resolve","trigger":{"type":"External"}},{"name":"timeout","trigger":{"type":"External"}},{"name":"success","trigger":{"type":"External"}},{"name":"failure","trigger":{"type":"External"}}],"transitions":[{"fromState":"Submitted","toState":"InProgress","trigger":"start","guard":"fields['assignee'] exists AND fields['assignee'] NOT eq ''"},{"fromState":"InProgress","toState":"SendingSurvey","trigger":"resolve","guard":"fields['resolutionDetail'] exists AND fields['resolutionDetail'] NOT eq ''","action":"health-check"},{"fromState":"SendingSurvey","toState":"Done","trigger":"success"},{"fromState":"SendingSurvey","toState":"SurveyNotSent","trigger":"failure"},{"fromState":"SendingSurvey","toState":"NotDone","trigger":"timeout"},{"fromState":"InProgress","toState":"NotDone","trigger":"cancel","guard":"fields['cancellationDetail'] exists AND fields['cancellationDetail'] NOT eq ''"}],"actions":[{"name":"health-check","runAsUserId":"user-id","actionDetails":{"type":"RunWorker","workerId":{"scope":"Health","code":"HealthCheckWorker"},"workerAsAt":"2022-01-01T01:02:03.0000000+00:00","workerParameters":{},"workerStatusTriggers":{"started":null,"completedWithResults":null,"completedNoResults":null,"failedToStart":null,"failedToComplete":null},"childTaskConfigurations":[{"taskDefinitionId":{"scope":"AAA","code":"BBB"},"mapStackingKeyFrom":null,"childTaskFields":{"assignee":{"mapFrom":"foo","setTo":"bar"}},"resultMatchingPattern":null,"taskDefinitionAsAt":null,"initialTrigger":"test-trigger"}]}}]}) # CreateTaskDefinitionRequest | The data to create a Task Definition

        try:
            # [EXPERIMENTAL] CreateTaskDefinition: Create a new Task Definition
            api_response = await api_instance.create_task_definition(create_task_definition_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TaskDefinitionsApi->create_task_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_task_definition_request** | [**CreateTaskDefinitionRequest**](CreateTaskDefinitionRequest.md)| The data to create a Task Definition | 

### Return type

[**TaskDefinition**](TaskDefinition.md)

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

# **delete_task_definition**
> DeletedEntityResponse delete_task_definition(scope, code)

[EXPERIMENTAL] DeleteTaskDefinition: Delete a Task Definition

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    TaskDefinitionsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TaskDefinitionsApi)
        scope = 'scope_example' # str | The scope that identifies a Task Definition
        code = 'code_example' # str | The code that identifies a Task Definition

        try:
            # [EXPERIMENTAL] DeleteTaskDefinition: Delete a Task Definition
            api_response = await api_instance.delete_task_definition(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TaskDefinitionsApi->delete_task_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Task Definition | 
 **code** | **str**| The code that identifies a Task Definition | 

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
**404** | Task Definition not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_task_definition**
> TaskDefinition get_task_definition(scope, code, as_at=as_at)

[EXPERIMENTAL] GetTaskDefinition: Get a Task Definition

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    TaskDefinitionsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TaskDefinitionsApi)
        scope = 'scope_example' # str | The scope that identifies a Task Definition
        code = 'code_example' # str | The code that identifies a Task Definition
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Task Definition. Defaults to returning the latest version of the Task Definition if not specified. (optional)

        try:
            # [EXPERIMENTAL] GetTaskDefinition: Get a Task Definition
            api_response = await api_instance.get_task_definition(scope, code, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TaskDefinitionsApi->get_task_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Task Definition | 
 **code** | **str**| The code that identifies a Task Definition | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Task Definition. Defaults to returning the latest version of the Task Definition if not specified. | [optional] 

### Return type

[**TaskDefinition**](TaskDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | Task Definition not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_task_definitions**
> PagedResourceListOfTaskDefinition list_task_definitions(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)

[EXPERIMENTAL] ListTaskDefinitions: List Task Definitions

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    TaskDefinitionsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TaskDefinitionsApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Task Definitions. Defaults to return the latest version of each Task Definition if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
        limit = 10 # int | When paginating, limit the number of returned results to this many. (optional) (default to 10)
        page = 'page_example' # str | The pagination token to use to continue listing task definitions from a previous call to list task definitions. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. (optional)

        try:
            # [EXPERIMENTAL] ListTaskDefinitions: List Task Definitions
            api_response = await api_instance.list_task_definitions(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TaskDefinitionsApi->list_task_definitions: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Task Definitions. Defaults to return the latest version of each Task Definition if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing task definitions from a previous call to list task definitions. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfTaskDefinition**](PagedResourceListOfTaskDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Task Definitions |  -  |
**400** | The details of the input related failure |  -  |
**404** | No Task Definitions found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_tasks_for_task_definition**
> ResourceListOfTask list_tasks_for_task_definition(scope, code, as_at=as_at)

[EXPERIMENTAL] ListTasksForTaskDefinition: List Tasks for a Task Definition

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    TaskDefinitionsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TaskDefinitionsApi)
        scope = 'scope_example' # str | The scope that identifies a Task Definition
        code = 'code_example' # str | The code that identifies a Task Definition
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Tasks. Defaults to return the latest version of each Task if not specified. (optional)

        try:
            # [EXPERIMENTAL] ListTasksForTaskDefinition: List Tasks for a Task Definition
            api_response = await api_instance.list_tasks_for_task_definition(scope, code, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TaskDefinitionsApi->list_tasks_for_task_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Task Definition | 
 **code** | **str**| The code that identifies a Task Definition | 
 **as_at** | **datetime**| The asAt datetime at which to list the Tasks. Defaults to return the latest version of each Task if not specified. | [optional] 

### Return type

[**ResourceListOfTask**](ResourceListOfTask.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No tasks found for this Task Definition. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_task_definition**
> TaskDefinition update_task_definition(scope, code, update_task_definition_request)

[EXPERIMENTAL] UpdateTaskDefinition: Update an existing Task Definition

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    TaskDefinitionsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TaskDefinitionsApi)
        scope = 'scope_example' # str | The scope that identifies a Task Definition
        code = 'code_example' # str | The code that identifies a Task Definition

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_task_definition_request = UpdateTaskDefinitionRequest()
        # update_task_definition_request = UpdateTaskDefinitionRequest.from_json("")
        update_task_definition_request = UpdateTaskDefinitionRequest.from_dict({"displayName":"An example TaskDefinition","description":"Test","states":[{"name":"Submitted"},{"name":"InProgress"},{"name":"SendingSurvey"},{"name":"Done"},{"name":"SurveyNotSent"},{"name":"NotDone"}],"fieldSchema":[{"name":"clientId","type":"String"},{"name":"assignee","type":"String","readOnlyStates":{"stateType":"SelectedStates","selectedStates":["Submitted","Done","SurveyNotSent","NotDone"]}},{"name":"resolutionDetail","type":"String","readOnlyStates":{"stateType":"TerminalState"}}],"initialState":{"name":"Submitted","requiredFields":["clientId"]},"triggers":[{"name":"start","trigger":{"type":"External"}},{"name":"cancel","trigger":{"type":"External"}},{"name":"resolve","trigger":{"type":"External"}},{"name":"timeout","trigger":{"type":"External"}},{"name":"success","trigger":{"type":"External"}},{"name":"failure","trigger":{"type":"External"}}],"transitions":[{"fromState":"Submitted","toState":"InProgress","trigger":"start","guard":"fields['assignee'] exists AND fields['assignee'] NOT eq ''"},{"fromState":"InProgress","toState":"SendingSurvey","trigger":"resolve","guard":"fields['resolutionDetail'] exists AND fields['resolutionDetail'] NOT eq ''","action":"health-check"},{"fromState":"SendingSurvey","toState":"Done","trigger":"success"},{"fromState":"SendingSurvey","toState":"SurveyNotSent","trigger":"failure"},{"fromState":"SendingSurvey","toState":"NotDone","trigger":"timeout"},{"fromState":"InProgress","toState":"NotDone","trigger":"cancel","guard":"fields['cancellationDetail'] exists AND fields['cancellationDetail'] NOT eq ''"}],"actions":[{"name":"health-check","runAsUserId":"user-id","actionDetails":{"type":"RunWorker","workerId":{"scope":"Health","code":"HealthCheckWorker"},"workerAsAt":"2022-01-01T01:02:03.0000000+00:00","workerParameters":{},"workerStatusTriggers":{"started":null,"completedWithResults":null,"completedNoResults":null,"failedToStart":null,"failedToComplete":null},"childTaskConfigurations":[{"taskDefinitionId":{"scope":"AAA","code":"BBB"},"mapStackingKeyFrom":null,"childTaskFields":{"assignee":{"mapFrom":"foo","setTo":"bar"}},"resultMatchingPattern":null,"taskDefinitionAsAt":null,"initialTrigger":"test-trigger"}]}}]}) # UpdateTaskDefinitionRequest | The data to update a Task Definition

        try:
            # [EXPERIMENTAL] UpdateTaskDefinition: Update an existing Task Definition
            api_response = await api_instance.update_task_definition(scope, code, update_task_definition_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TaskDefinitionsApi->update_task_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Task Definition | 
 **code** | **str**| The code that identifies a Task Definition | 
 **update_task_definition_request** | [**UpdateTaskDefinitionRequest**](UpdateTaskDefinitionRequest.md)| The data to update a Task Definition | 

### Return type

[**TaskDefinition**](TaskDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | Task Definition not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

