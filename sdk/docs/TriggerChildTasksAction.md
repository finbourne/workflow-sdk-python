# TriggerChildTasksAction

Defines a Trigger Child Tasks Action
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | 
**trigger** | **str** | Trigger on child tasks to be invoked | 
**filter** | **str** | Optional LUSID filter expression to limit the action to a subset of the child tasks | [optional] 
## Example

```python
from lusid_workflow.models.trigger_child_tasks_action import TriggerChildTasksAction
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
trigger: StrictStr = "example_trigger"
filter: Optional[StrictStr] = "example_filter"
trigger_child_tasks_action_instance = TriggerChildTasksAction(type=type, trigger=trigger, filter=filter)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

