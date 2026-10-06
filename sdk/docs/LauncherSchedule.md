# LauncherSchedule

When a Schedule Launcher starts a run of its Workflow
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_context** | **str** | The name of the calendar context the schedule is read in, which must be one the Launcher declares | 
**recurrence_pattern** | [**RecurrencePattern**](RecurrencePattern.md) |  | 
## Example

```python
from lusid_workflow.models.launcher_schedule import LauncherSchedule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

calendar_context: StrictStr = "example_calendar_context"
recurrence_pattern: RecurrencePattern = # Replace with your value
launcher_schedule_instance = LauncherSchedule(calendar_context=calendar_context, recurrence_pattern=recurrence_pattern)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

