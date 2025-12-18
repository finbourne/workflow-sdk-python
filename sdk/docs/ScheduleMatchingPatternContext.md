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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

time_zone: StrictStr = "example_time_zone"
holiday_calendars: Optional[List[CalendarReference]] = # Replace with your value
schedule_matching_pattern_context_instance = ScheduleMatchingPatternContext(time_zone=time_zone, holiday_calendars=holiday_calendars)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

