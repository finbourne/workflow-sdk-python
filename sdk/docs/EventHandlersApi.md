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

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_workflow
from lusid_workflow.rest import ApiException
from lusid_workflow.models.create_event_handler_request import CreateEventHandlerRequest
from lusid_workflow.models.event_handler import EventHandler
from pprint import pprint

import os
from lusid_workflow import (
    ApiClientFactory,
    EventHandlersApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid_workflow ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/workflow"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid_workflow.EventHandlersApi)
    create_event_handler_request = {"id":{"scope":"A1","code":"ZZZ"},"displayName":"An example Event Handler","description":"Test","status":"Active","eventMatchingPattern":{"eventType":"PortfolioCreated","filter":"body.portfolioScope eq 'TestScope'"},"runAsUserId":{"setTo":"ExampleUserId"},"taskDefinitionId":{"scope":"A1","code":"YYY"},"taskDefinitionAsAt":"9999-12-31T23:59:59.9999999+00:00","taskActivity":{"InitialTrigger":"InitialTrigger","Type":"CreateNewTask","CorrelationIds":[],"TaskFields":{}}} # CreateEventHandlerRequest | The data to create an Event Handler

    try:
        # [EXPERIMENTAL] CreateEventHandler: Create a new Event Handler
        api_response = await api_instance.create_event_handler(create_event_handler_request)
        print("The response of EventHandlersApi->create_event_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHandlersApi->create_event_handler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_event_handler_request** | [**CreateEventHandlerRequest**](CreateEventHandlerRequest.md)| The data to create an Event Handler | 

### Return type

[**EventHandler**](EventHandler.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_handler**
> DeletedEntityResponse delete_event_handler(scope, code)

[EXPERIMENTAL] DeleteEventHandler: Delete an Event Handler

If the Event Handler does not exist a failure will be returned

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_workflow
from lusid_workflow.rest import ApiException
from lusid_workflow.models.deleted_entity_response import DeletedEntityResponse
from pprint import pprint

import os
from lusid_workflow import (
    ApiClientFactory,
    EventHandlersApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid_workflow ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/workflow"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid_workflow.EventHandlersApi)
    scope = 'scope_example' # str | Scope of the event handler to be deleted
    code = 'code_example' # str | Code of the event handler to be deleted

    try:
        # [EXPERIMENTAL] DeleteEventHandler: Delete an Event Handler
        api_response = await api_instance.delete_event_handler(scope, code)
        print("The response of EventHandlersApi->delete_event_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHandlersApi->delete_event_handler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the event handler to be deleted | 
 **code** | **str**| Code of the event handler to be deleted | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_handler**
> EventHandler get_event_handler(scope, code, as_at=as_at)

[EXPERIMENTAL] GetEventHandler: Get an Event Handler

Will return a NotFound failure if the event handler does not exist

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_workflow
from lusid_workflow.rest import ApiException
from lusid_workflow.models.event_handler import EventHandler
from pprint import pprint

import os
from lusid_workflow import (
    ApiClientFactory,
    EventHandlersApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid_workflow ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/workflow"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid_workflow.EventHandlersApi)
    scope = 'scope_example' # str | Scope of the event handler
    code = 'code_example' # str | Code of the event handler
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the event handler. Defaults to returning the latest version of the event handler if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetEventHandler: Get an Event Handler
        api_response = await api_instance.get_event_handler(scope, code, as_at=as_at)
        print("The response of EventHandlersApi->get_event_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHandlersApi->get_event_handler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the event handler | 
 **code** | **str**| Code of the event handler | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the event handler. Defaults to returning the latest version of the event handler if not specified. | [optional] 

### Return type

[**EventHandler**](EventHandler.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_handlers**
> PagedResourceListOfEventHandler list_event_handlers(as_at=as_at, filter=filter, limit=limit, page=page)

[EXPERIMENTAL] ListEventHandlers: List Event Handlers

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_workflow
from lusid_workflow.rest import ApiException
from lusid_workflow.models.paged_resource_list_of_event_handler import PagedResourceListOfEventHandler
from pprint import pprint

import os
from lusid_workflow import (
    ApiClientFactory,
    EventHandlersApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid_workflow ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/workflow"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid_workflow.EventHandlersApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Event Handlers. Defaults to return the latest version of each Event Handler if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. (optional)
    limit = 10 # int | When paginating, limit the number of returned results to this many. (optional) (default to 10)
    page = 'page_example' # str | The pagination token to use to continue listing event handlers from a previous call to list event handlers. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. (optional)

    try:
        # [EXPERIMENTAL] ListEventHandlers: List Event Handlers
        api_response = await api_instance.list_event_handlers(as_at=as_at, filter=filter, limit=limit, page=page)
        print("The response of EventHandlersApi->list_event_handlers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHandlersApi->list_event_handlers: %s\n" % e)
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

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Event Handlers |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_handler**
> EventHandler update_event_handler(scope, code, update_event_handler_request)

[EXPERIMENTAL] UpdateEventHandler: Update an existing Event handler

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_workflow
from lusid_workflow.rest import ApiException
from lusid_workflow.models.event_handler import EventHandler
from lusid_workflow.models.update_event_handler_request import UpdateEventHandlerRequest
from pprint import pprint

import os
from lusid_workflow import (
    ApiClientFactory,
    EventHandlersApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid_workflow ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/workflow"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid_workflow.EventHandlersApi)
    scope = 'scope_example' # str | The scope that identifies an Event Handler
    code = 'code_example' # str | The code that identifies an Event Handler
    update_event_handler_request = {"displayName":"An example Event Handler","description":"Test","status":"Active","eventMatchingPattern":{"eventType":"PortfolioCreated","filter":"body.portfolioScope eq 'TestScope'"},"runAsUserId":{"setTo":"ExampleUserId"},"taskDefinitionId":{"scope":"A1","code":"YYY"},"taskDefinitionAsAt":"9999-12-31T23:59:59.9999999+00:00","taskActivity":{"InitialTrigger":"InitialTrigger","Type":"CreateNewTask","CorrelationIds":[],"TaskFields":{}}} # UpdateEventHandlerRequest | The data to update an Event Handler

    try:
        # [EXPERIMENTAL] UpdateEventHandler: Update an existing Event handler
        api_response = await api_instance.update_event_handler(scope, code, update_event_handler_request)
        print("The response of EventHandlersApi->update_event_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHandlersApi->update_event_handler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies an Event Handler | 
 **code** | **str**| The code that identifies an Event Handler | 
 **update_event_handler_request** | [**UpdateEventHandlerRequest**](UpdateEventHandlerRequest.md)| The data to update an Event Handler | 

### Return type

[**EventHandler**](EventHandler.md)

### Authorization

[oauth2](../README.md#oauth2)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

