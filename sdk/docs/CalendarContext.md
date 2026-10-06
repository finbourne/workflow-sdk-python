# CalendarContext

A named time zone and set of holiday calendars.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name the schedule and the date and time adjustments use to name this context | 
**time_zone** | **str** | The time zone to use. A TZ identifier, for example \&quot;Europe/London\&quot; | 
**holiday_calendars** | [**List[CalendarReference]**](CalendarReference.md) | The holiday calendars that decide which dates are business days in this context | [optional] 
## Example

```python
from lusid_workflow.models.calendar_context import CalendarContext
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
time_zone: StrictStr = "example_time_zone"
holiday_calendars: Optional[List[CalendarReference]] = # Replace with your value
calendar_context_instance = CalendarContext(name=name, time_zone=time_zone, holiday_calendars=holiday_calendars)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

