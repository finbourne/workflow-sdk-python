# Worker

Information about the Worker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**worker_configuration** | [**WorkerConfigurationResponse**](WorkerConfigurationResponse.md) |  | 
**version** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
**parameters** | [**List[Parameter]**](Parameter.md) | The Parameters this Worker accepts or requires. | [optional] 
**result_fields** | [**List[ResultField]**](ResultField.md) | The Fields that the Worker results will come back with. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid_workflow.models.worker import Worker

# TODO update the JSON string below
json = "{}"
# create an instance of Worker from a JSON string
worker_instance = Worker.from_json(json)
# print the JSON string representation of the object
print Worker.to_json()

# convert the object into a dict
worker_dict = worker_instance.to_dict()
# create an instance of Worker from a dict
worker_form_dict = worker.from_dict(worker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


