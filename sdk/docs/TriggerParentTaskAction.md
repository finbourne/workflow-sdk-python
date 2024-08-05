# TriggerParentTaskAction

Defines a Trigger Parent Task Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | 
**trigger** | **str** | Trigger on parent task to be invoked | 

## Example

```python
from lusid_workflow.models.trigger_parent_task_action import TriggerParentTaskAction

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerParentTaskAction from a JSON string
trigger_parent_task_action_instance = TriggerParentTaskAction.from_json(json)
# print the JSON string representation of the object
print TriggerParentTaskAction.to_json()

# convert the object into a dict
trigger_parent_task_action_dict = trigger_parent_task_action_instance.to_dict()
# create an instance of TriggerParentTaskAction from a dict
trigger_parent_task_action_form_dict = trigger_parent_task_action.from_dict(trigger_parent_task_action_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


