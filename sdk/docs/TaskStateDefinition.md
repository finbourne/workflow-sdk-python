# TaskStateDefinition

A Task Definition/Task has a given set of States

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of this State | 
**display_name** | **str** | The display name of this State | [optional] 
**description** | **str** | The description of this State | [optional] 
**category** | **str** | The category of this State | [optional] 

## Example

```python
from lusid_workflow.models.task_state_definition import TaskStateDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStateDefinition from a JSON string
task_state_definition_instance = TaskStateDefinition.from_json(json)
# print the JSON string representation of the object
print TaskStateDefinition.to_json()

# convert the object into a dict
task_state_definition_dict = task_state_definition_instance.to_dict()
# create an instance of TaskStateDefinition from a dict
task_state_definition_form_dict = task_state_definition.from_dict(task_state_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


