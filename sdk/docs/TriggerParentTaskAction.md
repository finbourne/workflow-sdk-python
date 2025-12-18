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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
trigger: StrictStr = "example_trigger"
trigger_parent_task_action_instance = TriggerParentTaskAction(type=type, trigger=trigger)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

