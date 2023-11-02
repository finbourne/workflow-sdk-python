# UpdateTaskRequest

A request to update a Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_ids** | **List[str]** | A set of guid identifiers that allow correlation across the application tier | [optional] 
**fields** | [**List[TaskInstanceField]**](TaskInstanceField.md) | Defines the fields associated with the update | [optional] 

## Example

```python
from lusid_workflow.models.update_task_request import UpdateTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaskRequest from a JSON string
update_task_request_instance = UpdateTaskRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTaskRequest.to_json()

# convert the object into a dict
update_task_request_dict = update_task_request_instance.to_dict()
# create an instance of UpdateTaskRequest from a dict
update_task_request_form_dict = update_task_request.from_dict(update_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


