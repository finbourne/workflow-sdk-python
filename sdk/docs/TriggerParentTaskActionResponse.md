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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
trigger: Optional[StrictStr] = "example_trigger"
trigger_parent_task_action_response_instance = TriggerParentTaskActionResponse(type=type, trigger=trigger)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

