# UpdateWorkerRequest

Request to Update a new worker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**worker_configuration** | **object** | Information about how the worker should be executed | 

## Example

```python
from lusid_workflow.models.update_worker_request import UpdateWorkerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkerRequest from a JSON string
update_worker_request_instance = UpdateWorkerRequest.from_json(json)
# print the JSON string representation of the object
print UpdateWorkerRequest.to_json()

# convert the object into a dict
update_worker_request_dict = update_worker_request_instance.to_dict()
# create an instance of UpdateWorkerRequest from a dict
update_worker_request_form_dict = update_worker_request.from_dict(update_worker_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


