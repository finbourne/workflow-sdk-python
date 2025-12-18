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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
states: List[TaskStateDefinition] = # Replace with your value
field_schema: Optional[List[TaskFieldDefinition]] = # Replace with your value
initial_state: InitialState = # Replace with your value
triggers: Optional[List[TransitionTriggerDefinition]] = # Replace with your value
transitions: Optional[List[TaskTransitionDefinition]] = # Replace with your value
actions: Optional[List[ActionDefinition]] = # Replace with your value
create_task_definition_request_instance = CreateTaskDefinitionRequest(id=id, display_name=display_name, description=description, states=states, field_schema=field_schema, initial_state=initial_state, triggers=triggers, transitions=transitions, actions=actions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

