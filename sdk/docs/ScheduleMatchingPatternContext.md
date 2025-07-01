# ScheduleMatchingPatternContext

Context for a Schedule Matching Pattern
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zone** | **str** | The time zone to use | 
**holiday_calendars** | [**List[CalendarReference]**](CalendarReference.md) | References to any Holiday Calendars to use | [optional] 
## Example

```python
from lusid_workflow.models.schedule_matching_pattern_context import ScheduleMatchingPatternContext
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

time_zone: StrictStr = "example_time_zone"
holiday_calendars: Optional[conlist(CalendarReference, max_items=5, min_items=0)] = Field(None, alias="holidayCalendars", description="References to any Holiday Calendars to use")
schedule_matching_pattern_context_instance = ScheduleMatchingPatternContext(time_zone=time_zone, holiday_calendars=holiday_calendars)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

