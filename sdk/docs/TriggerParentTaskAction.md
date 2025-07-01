# TriggerParentTaskAction

Defines a Trigger Parent Task Action
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | 
**trigger** | **str** | Trigger on parent task to be invoked | 
## Example

```python
from lusid_workflow.models.trigger_parent_task_action import TriggerParentTaskAction
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

type: StrictStr = "example_type"
trigger: StrictStr = "example_trigger"
trigger_parent_task_action_instance = TriggerParentTaskAction(type=type, trigger=trigger)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

