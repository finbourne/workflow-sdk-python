# lusid_workflow.EventHandlersApi

All URIs are relative to *https://fbn-prd.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_handler**](EventHandlersApi.md#create_event_handler) | **POST** /api/eventhandlers | [EXPERIMENTAL] CreateEventHandler: Create a new Event Handler
[**delete_event_handler**](EventHandlersApi.md#delete_event_handler) | **DELETE** /api/eventhandlers/{scope}/{code} | [EXPERIMENTAL] DeleteEventHandler: Delete an Event Handler
[**get_event_handler**](EventHandlersApi.md#get_event_handler) | **GET** /api/eventhandlers/{scope}/{code} | [EXPERIMENTAL] GetEventHandler: Get an Event Handler
[**list_event_handlers**](EventHandlersApi.md#list_event_handlers) | **GET** /api/eventhandlers | [EXPERIMENTAL] ListEventHandlers: List Event Handlers
[**update_event_handler**](EventHandlersApi.md#update_event_handler) | **PUT** /api/eventhandlers/{scope}/{code} | [EXPERIMENTAL] UpdateEventHandler: Update an existing Event handler


# **create_event_handler**
> EventHandler create_event_handler(create_event_handler_request)

[EXPERIMENTAL] CreateEventHandler: Create a new Event Handler

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    EventHandlersApi
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
        api_instance = api_client_factory.build(EventHandlersApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_event_handler_request = CreateEventHandlerRequest()
        # create_event_handler_request = CreateEventHandlerRequest.from_json("")
        create_event_handler_request = CreateEventHandlerRequest.from_dict({"id":{"scope":"A1","code":"ZZZ"},"displayName":"An example Event Handler","description":"Test","status":"Active","eventMatchingPattern":{"eventType":"PortfolioCreated","filter":"body.portfolioScope eq 'TestScope'"},"runAsUserId":{"setTo":"ExampleUserId"},"taskDefinitionId":{"scope":"A1","code":"YYY"},"taskDefinitionAsAt":"9999-12-31T23:59:59.9999999+00:00","taskActivity":{"initialTrigger":"InitialTrigger","type":"CreateNewTask","correlationIds":[],"taskFields":{}}}) # CreateEventHandlerRequest | The data to create an Event Handler

        try:
            # [EXPERIMENTAL] CreateEventHandler: Create a new Event Handler
            api_response = await api_instance.create_event_handler(create_event_handler_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling EventHandlersApi->create_event_handler: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_event_handler_request** | [**CreateEventHandlerRequest**](CreateEventHandlerRequest.md)| The data to create an Event Handler | 

### Return type

[**EventHandler**](EventHandler.md)

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

# **delete_event_handler**
> DeletedEntityResponse delete_event_handler(scope, code)

[EXPERIMENTAL] DeleteEventHandler: Delete an Event Handler

If the Event Handler does not exist a failure will be returned

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    EventHandlersApi
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
        api_instance = api_client_factory.build(EventHandlersApi)
        scope = 'scope_example' # str | Scope of the event handler to be deleted
        code = 'code_example' # str | Code of the event handler to be deleted

        try:
            # [EXPERIMENTAL] DeleteEventHandler: Delete an Event Handler
            api_response = await api_instance.delete_event_handler(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling EventHandlersApi->delete_event_handler: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the event handler to be deleted | 
 **code** | **str**| Code of the event handler to be deleted | 

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
**404** | Event Handler not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_event_handler**
> EventHandler get_event_handler(scope, code, as_at=as_at)

[EXPERIMENTAL] GetEventHandler: Get an Event Handler

Will return a NotFound failure if the event handler does not exist

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    EventHandlersApi
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
        api_instance = api_client_factory.build(EventHandlersApi)
        scope = 'scope_example' # str | Scope of the event handler
        code = 'code_example' # str | Code of the event handler
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the event handler. Defaults to returning the latest version of the event handler if not specified. (optional)

        try:
            # [EXPERIMENTAL] GetEventHandler: Get an Event Handler
            api_response = await api_instance.get_event_handler(scope, code, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling EventHandlersApi->get_event_handler: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the event handler | 
 **code** | **str**| Code of the event handler | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the event handler. Defaults to returning the latest version of the event handler if not specified. | [optional] 

### Return type

[**EventHandler**](EventHandler.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_event_handlers**
> PagedResourceListOfEventHandler list_event_handlers(as_at=as_at, filter=filter, limit=limit, page=page)

[EXPERIMENTAL] ListEventHandlers: List Event Handlers

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    EventHandlersApi
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
        api_instance = api_client_factory.build(EventHandlersApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Event Handlers. Defaults to return the latest version of each Event Handler if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. (optional)
        limit = 10 # int | When paginating, limit the number of returned results to this many. (optional) (default to 10)
        page = 'page_example' # str | The pagination token to use to continue listing event handlers from a previous call to list event handlers. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. (optional)

        try:
            # [EXPERIMENTAL] ListEventHandlers: List Event Handlers
            api_response = await api_instance.list_event_handlers(as_at=as_at, filter=filter, limit=limit, page=page)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling EventHandlersApi->list_event_handlers: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Event Handlers. Defaults to return the latest version of each Event Handler if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing event handlers from a previous call to list event handlers. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfEventHandler**](PagedResourceListOfEventHandler.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Event Handlers |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_event_handler**
> EventHandler update_event_handler(scope, code, update_event_handler_request)

[EXPERIMENTAL] UpdateEventHandler: Update an existing Event handler

### Example

```python
import asyncio
from lusid_workflow.exceptions import ApiException
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    ApiClientFactory,
    EventHandlersApi
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
        api_instance = api_client_factory.build(EventHandlersApi)
        scope = 'scope_example' # str | The scope that identifies an Event Handler
        code = 'code_example' # str | The code that identifies an Event Handler

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_event_handler_request = UpdateEventHandlerRequest()
        # update_event_handler_request = UpdateEventHandlerRequest.from_json("")
        update_event_handler_request = UpdateEventHandlerRequest.from_dict({"displayName":"An example Event Handler","description":"Test","status":"Active","eventMatchingPattern":{"eventType":"PortfolioCreated","filter":"body.portfolioScope eq 'TestScope'"},"runAsUserId":{"setTo":"ExampleUserId"},"taskDefinitionId":{"scope":"A1","code":"YYY"},"taskDefinitionAsAt":"9999-12-31T23:59:59.9999999+00:00","taskActivity":{"initialTrigger":"InitialTrigger","type":"CreateNewTask","correlationIds":[],"taskFields":{}}}) # UpdateEventHandlerRequest | The data to update an Event Handler

        try:
            # [EXPERIMENTAL] UpdateEventHandler: Update an existing Event handler
            api_response = await api_instance.update_event_handler(scope, code, update_event_handler_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling EventHandlersApi->update_event_handler: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies an Event Handler | 
 **code** | **str**| The code that identifies an Event Handler | 
 **update_event_handler_request** | [**UpdateEventHandlerRequest**](UpdateEventHandlerRequest.md)| The data to update an Event Handler | 

### Return type

[**EventHandler**](EventHandler.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | Event Handler not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

