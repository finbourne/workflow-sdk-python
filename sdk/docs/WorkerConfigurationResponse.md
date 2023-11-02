# WorkerConfigurationResponse

Readonly information about how the worker should be executed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | 
**url** | **str** | The URL to check, eg: https://www.google.com/ | [optional] 
**name** | **str** | Name of the view in Luminesce | [optional] 

## Example

```python
from lusid_workflow.models.worker_configuration_response import WorkerConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkerConfigurationResponse from a JSON string
worker_configuration_response_instance = WorkerConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print WorkerConfigurationResponse.to_json()

# convert the object into a dict
worker_configuration_response_dict = worker_configuration_response_instance.to_dict()
# create an instance of WorkerConfigurationResponse from a dict
worker_configuration_response_form_dict = worker_configuration_response.from_dict(worker_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


