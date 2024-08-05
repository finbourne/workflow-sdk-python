# TriggerParentTaskActionResponse

Defines a read-only Trigger Parent Task Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | [optional] 
**trigger** | **str** | Trigger on parent task to be invoked | [optional] 

## Example

```python
from lusid_workflow.models.trigger_parent_task_action_response import TriggerParentTaskActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerParentTaskActionResponse from a JSON string
trigger_parent_task_action_response_instance = TriggerParentTaskActionResponse.from_json(json)
# print the JSON string representation of the object
print TriggerParentTaskActionResponse.to_json()

# convert the object into a dict
trigger_parent_task_action_response_dict = trigger_parent_task_action_response_instance.to_dict()
# create an instance of TriggerParentTaskActionResponse from a dict
trigger_parent_task_action_response_form_dict = trigger_parent_task_action_response.from_dict(trigger_parent_task_action_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


