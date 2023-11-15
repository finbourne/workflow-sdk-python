# CreateTaskRequest

Contains required info to create a new Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**correlation_ids** | **List[str]** | A set of guid identifiers that allow correlation across the application tier | [optional] 
**fields** | [**List[TaskInstanceField]**](TaskInstanceField.md) | Fields and their initial values - should correspond with the Task Definition field schema | [optional] 
**stacking_key** | **str** | The key for the Stack that this Task should be added to | [optional] 

## Example

```python
from lusid_workflow.models.create_task_request import CreateTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaskRequest from a JSON string
create_task_request_instance = CreateTaskRequest.from_json(json)
# print the JSON string representation of the object
print CreateTaskRequest.to_json()

# convert the object into a dict
create_task_request_dict = create_task_request_instance.to_dict()
# create an instance of CreateTaskRequest from a dict
create_task_request_form_dict = create_task_request.from_dict(create_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


