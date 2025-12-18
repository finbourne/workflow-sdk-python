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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

from_state: StrictStr = "example_from_state"
to_state: StrictStr = "example_to_state"
trigger: StrictStr = "example_trigger"
guard: Optional[StrictStr] = "example_guard"
action: Optional[StrictStr] = "example_action"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
guard_description: Optional[StrictStr] = "example_guard_description"
guard_condition_not_met_message: Optional[StrictStr] = "example_guard_condition_not_met_message"
task_transition_definition_instance = TaskTransitionDefinition(from_state=from_state, to_state=to_state, trigger=trigger, guard=guard, action=action, display_name=display_name, description=description, guard_description=guard_description, guard_condition_not_met_message=guard_condition_not_met_message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

