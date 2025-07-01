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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

id: ResourceId = # Replace with your value
version: Optional[VersionInfo] = None
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
states: conlist(TaskStateDefinition, min_items=1) = Field(..., description="The states this Task Definition operates over")
field_schema: Optional[conlist(TaskFieldDefinition)] = # Replace with your value
initial_state: InitialState = # Replace with your value
triggers: Optional[conlist(TransitionTriggerDefinition)] = # Replace with your value
actions: Optional[conlist(ActionDefinitionResponse)] = # Replace with your value
transitions: Optional[conlist(TaskTransitionDefinition)] = # Replace with your value
task_definition_instance = TaskDefinition(id=id, version=version, display_name=display_name, description=description, states=states, field_schema=field_schema, initial_state=initial_state, triggers=triggers, actions=actions, transitions=transitions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

