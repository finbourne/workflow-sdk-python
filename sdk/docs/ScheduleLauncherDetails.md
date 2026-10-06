# ScheduleLauncherDetails

A Launcher that starts a run of its Workflow at the times a recurrence pattern gives, and can fill date and time fields of the root task from the instant it fired
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**launcher_type** | **str** |  | 
**schedule** | [**LauncherSchedule**](LauncherSchedule.md) |  | 
**calendar_contexts** | [**List[CalendarContext]**](CalendarContext.md) | The named time zones and holiday calendars this Launcher works in.              Only a Schedule Launcher works in a calendar context | [optional] 
**map_task_fields** | [**Dict[str, ScheduleTaskFieldMapping]**](ScheduleTaskFieldMapping.md) | Fields of the root task filled from the instant the schedule fired, keyed by the field name on the root task definition | [optional] 
**run_as_user_id** | [**LauncherMapping**](LauncherMapping.md) |  | 
**set_task_fields** | **Dict[str, Optional[object]]** | Fields of the root task set to a fixed value, keyed by the field name on the root task definition | [optional] 
**set_correlation_ids** | **List[str]** | Correlation IDs put on the root task as given | [optional] 
**initial_trigger** | **str** | The trigger given to the root task once it is made and all of its fields are filled. When it is left out the root task is left in its initial state | [optional] 
## Example

```python
from lusid_workflow.models.schedule_launcher_details import ScheduleLauncherDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

launcher_type: StrictStr = "example_launcher_type"
schedule: LauncherSchedule
calendar_contexts: Optional[List[CalendarContext]] = # Replace with your value
map_task_fields: Optional[Dict[str, ScheduleTaskFieldMapping]] = # Replace with your value
run_as_user_id: LauncherMapping = # Replace with your value
set_task_fields: Optional[Dict[str, Any]] = # Replace with your value
set_correlation_ids: Optional[List[StrictStr]] = # Replace with your value
initial_trigger: Optional[StrictStr] = "example_initial_trigger"
schedule_launcher_details_instance = ScheduleLauncherDetails(launcher_type=launcher_type, schedule=schedule, calendar_contexts=calendar_contexts, map_task_fields=map_task_fields, run_as_user_id=run_as_user_id, set_task_fields=set_task_fields, set_correlation_ids=set_correlation_ids, initial_trigger=initial_trigger)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

