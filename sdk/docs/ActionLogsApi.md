# lusid_workflow.ActionLogsApi

All URIs are relative to *https://fbn-prd.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_action_logs**](ActionLogsApi.md#get_action_logs) | **GET** /api/actionlogs/{id} | [EXPERIMENTAL] GetActionLogs: Get the Action Logs for an Action Id


# **get_action_logs**
> ActionLog get_action_logs(id)

[EXPERIMENTAL] GetActionLogs: Get the Action Logs for an Action Id

### Example

```python
from lusid_workflow.exceptions import ApiException
from lusid_workflow.extensions.configuration_options import ConfigurationOptions
from lusid_workflow.models import *
from pprint import pprint
from lusid_workflow import (
    SyncApiClientFactory,
    ActionLogsApi
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
    api_instance = api_client_factory.build(ActionLogsApi)
    id = 'id_example' # str | The Action Id

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_action_logs(id, opts=opts)

        # [EXPERIMENTAL] GetActionLogs: Get the Action Logs for an Action Id
        api_response = api_instance.get_action_logs(id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ActionLogsApi->get_action_logs: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Action Id | 

### Return type

[**ActionLog**](ActionLog.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | Action Log not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

