# UpdateTaskDefinitionRequest

Contains required info to update a Task Definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**states** | [**List[TaskStateDefinition]**](TaskStateDefinition.md) | The states this Task Definition operates over | 
**field_schema** | [**List[TaskFieldDefinition]**](TaskFieldDefinition.md) | Defines the fields associated with this Task | [optional] 
**initial_state** | [**InitialState**](InitialState.md) |  | 
**triggers** | [**List[TransitionTriggerDefinition]**](TransitionTriggerDefinition.md) | Triggers | [optional] 
**transitions** | [**List[TaskTransitionDefinition]**](TaskTransitionDefinition.md) | Transitions | [optional] 
**actions** | [**List[ActionDefinition]**](ActionDefinition.md) | Actions | [optional] 

## Example

```python
from lusid_workflow.models.update_task_definition_request import UpdateTaskDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaskDefinitionRequest from a JSON string
update_task_definition_request_instance = UpdateTaskDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTaskDefinitionRequest.to_json()

# convert the object into a dict
update_task_definition_request_dict = update_task_definition_request_instance.to_dict()
# create an instance of UpdateTaskDefinitionRequest from a dict
update_task_definition_request_form_dict = update_task_definition_request.from_dict(update_task_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


