# TaskTransitionDefinition

Defines a State change

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_state** | **str** | The State this Transition if coming From | 
**to_state** | **str** | The State this Transition is going To | 
**trigger** | **str** | The Trigger for this Transition | 
**guard** | **str** | The Guard for this Transition, if any | [optional] 
**action** | **str** | The Action to invoke on successful Transition | [optional] 
**display_name** | **str** | Display name for transition | [optional] 
**description** | **str** | Description for transition | [optional] 
**guard_description** | **str** | Guard description for transition | [optional] 
**guard_condition_not_met_message** | **str** | Message when guard has not been met | [optional] 

## Example

```python
from lusid_workflow.models.task_transition_definition import TaskTransitionDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTransitionDefinition from a JSON string
task_transition_definition_instance = TaskTransitionDefinition.from_json(json)
# print the JSON string representation of the object
print TaskTransitionDefinition.to_json()

# convert the object into a dict
task_transition_definition_dict = task_transition_definition_instance.to_dict()
# create an instance of TaskTransitionDefinition from a dict
task_transition_definition_form_dict = task_transition_definition.from_dict(task_transition_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


