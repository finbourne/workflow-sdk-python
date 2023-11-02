# TaskDefinition

Task Definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**version** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**states** | [**List[TaskStateDefinition]**](TaskStateDefinition.md) | The states this Task Definition operates over | 
**field_schema** | [**List[TaskFieldDefinition]**](TaskFieldDefinition.md) | The Fields that this Task Definition operates on | [optional] 
**initial_state** | [**InitialState**](InitialState.md) |  | 
**triggers** | [**List[TransitionTriggerDefinition]**](TransitionTriggerDefinition.md) | The Triggers for State transition | [optional] 
**actions** | [**List[ActionDefinitionResponse]**](ActionDefinitionResponse.md) | The Actions of this Task - executed after a Transition completion | [optional] 
**transitions** | [**List[TaskTransitionDefinition]**](TaskTransitionDefinition.md) | The Transitions between States | [optional] 

## Example

```python
from lusid_workflow.models.task_definition import TaskDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of TaskDefinition from a JSON string
task_definition_instance = TaskDefinition.from_json(json)
# print the JSON string representation of the object
print TaskDefinition.to_json()

# convert the object into a dict
task_definition_dict = task_definition_instance.to_dict()
# create an instance of TaskDefinition from a dict
task_definition_form_dict = task_definition.from_dict(task_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


