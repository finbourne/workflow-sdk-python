# TriggerParentTaskActionResponse

Defines a read-only Trigger Parent Task Action
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | [optional] 
**trigger** | **str** | Trigger on parent task to be invoked | [optional] 
## Example

```python
from lusid_workflow.models.trigger_parent_task_action_response import TriggerParentTaskActionResponse
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator

type: Optional[StrictStr] = "example_type"
trigger: Optional[StrictStr] = "example_trigger"
trigger_parent_task_action_response_instance = TriggerParentTaskActionResponse(type=type, trigger=trigger)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

