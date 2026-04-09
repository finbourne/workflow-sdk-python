# TriggerChildTasksActionResponse

Defines a read-only Trigger Child Tasks Action
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | [optional] 
**trigger** | **str** | Trigger on child tasks to be invoked | [optional] 
## Example

```python
from lusid_workflow.models.trigger_child_tasks_action_response import TriggerChildTasksActionResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
trigger: Optional[StrictStr] = "example_trigger"
trigger_child_tasks_action_response_instance = TriggerChildTasksActionResponse(type=type, trigger=trigger)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

