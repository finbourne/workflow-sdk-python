# UpdateTaskWithIdAndTriggerRequest

A request to update multiple Tasks  Includes a trigger which is supplied from route in single update request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_instance_id** | **str** | The ID of the task instance | [optional] 
**correlation_ids** | **List[str]** | A set of guid identifiers that allow correlation across the application tier | [optional] 
**fields** | [**List[TaskInstanceField]**](TaskInstanceField.md) | Defines the fields associated with the update | [optional] 
**stacking_key** | **str** | The key for the Stack that this Task should be added to | [optional] 
**trigger_name** | **str** | The trigger we want to update the task with | [optional] 

## Example

```python
from lusid_workflow.models.update_task_with_id_and_trigger_request import UpdateTaskWithIdAndTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaskWithIdAndTriggerRequest from a JSON string
update_task_with_id_and_trigger_request_instance = UpdateTaskWithIdAndTriggerRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTaskWithIdAndTriggerRequest.to_json()

# convert the object into a dict
update_task_with_id_and_trigger_request_dict = update_task_with_id_and_trigger_request_instance.to_dict()
# create an instance of UpdateTaskWithIdAndTriggerRequest from a dict
update_task_with_id_and_trigger_request_form_dict = update_task_with_id_and_trigger_request.from_dict(update_task_with_id_and_trigger_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


