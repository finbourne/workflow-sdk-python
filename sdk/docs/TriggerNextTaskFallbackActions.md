# TriggerNextTaskFallbackActions

Actions on the same task definition that a Trigger Next Task action runs instead of triggering the next task
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_of_sequence** | **str** | Run when this task has no next task to trigger | [optional] 
**next_task_error** | **str** | Run when the next task cannot be triggered, e.g. it was deleted or is not in its initial state | [optional] 
## Example

```python
from lusid_workflow.models.trigger_next_task_fallback_actions import TriggerNextTaskFallbackActions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

end_of_sequence: Optional[StrictStr] = "example_end_of_sequence"
next_task_error: Optional[StrictStr] = "example_next_task_error"
trigger_next_task_fallback_actions_instance = TriggerNextTaskFallbackActions(end_of_sequence=end_of_sequence, next_task_error=next_task_error)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

