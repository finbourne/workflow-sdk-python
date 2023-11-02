# CreateWorkerRequest

Request to Create a new worker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**worker_configuration** | [**WorkerConfiguration**](WorkerConfiguration.md) |  | 

## Example

```python
from lusid_workflow.models.create_worker_request import CreateWorkerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkerRequest from a JSON string
create_worker_request_instance = CreateWorkerRequest.from_json(json)
# print the JSON string representation of the object
print CreateWorkerRequest.to_json()

# convert the object into a dict
create_worker_request_dict = create_worker_request_instance.to_dict()
# create an instance of CreateWorkerRequest from a dict
create_worker_request_form_dict = create_worker_request.from_dict(create_worker_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


