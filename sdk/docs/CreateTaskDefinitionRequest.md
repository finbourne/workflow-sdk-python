# CreateTaskDefinitionRequest

Contains required info to create a new Task Definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
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
from lusid_workflow.models.create_task_definition_request import CreateTaskDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaskDefinitionRequest from a JSON string
create_task_definition_request_instance = CreateTaskDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print CreateTaskDefinitionRequest.to_json()

# convert the object into a dict
create_task_definition_request_dict = create_task_definition_request_instance.to_dict()
# create an instance of CreateTaskDefinitionRequest from a dict
create_task_definition_request_form_dict = create_task_definition_request.from_dict(create_task_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


