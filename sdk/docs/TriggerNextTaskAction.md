# TriggerNextTaskAction

Defines a Trigger Next Task Action
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | 
**default_trigger** | **str** | Trigger sent to the next task when this task has no nextTaskInitialTrigger of its own | [optional] 
**fallback_actions** | [**TriggerNextTaskFallbackActions**](TriggerNextTaskFallbackActions.md) |  | [optional] 
## Example

```python
from lusid_workflow.models.trigger_next_task_action import TriggerNextTaskAction
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
default_trigger: Optional[StrictStr] = "example_default_trigger"
fallback_actions: Optional[TriggerNextTaskFallbackActions] = # Replace with your value
trigger_next_task_action_instance = TriggerNextTaskAction(type=type, default_trigger=default_trigger, fallback_actions=fallback_actions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

