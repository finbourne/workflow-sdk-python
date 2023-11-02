# WorkerConfiguration

Information about how the worker should be executed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | 
**url** | **str** | The URL to check, eg: https://www.google.com/ | 
**name** | **str** | Name of the view in Luminesce | 

## Example

```python
from lusid_workflow.models.worker_configuration import WorkerConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of WorkerConfiguration from a JSON string
worker_configuration_instance = WorkerConfiguration.from_json(json)
# print the JSON string representation of the object
print WorkerConfiguration.to_json()

# convert the object into a dict
worker_configuration_dict = worker_configuration_instance.to_dict()
# create an instance of WorkerConfiguration from a dict
worker_configuration_form_dict = worker_configuration.from_dict(worker_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


