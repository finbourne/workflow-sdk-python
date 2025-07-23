# ScheduledTimeAdjustment

Represents an adjustment to the scheduled time of an EventHandler. Only relevant for EventHandlers with a  Finbourne.Workflow.WebApi.Common.Dto.Json.EventHandlers.ScheduleMatchingPattern
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_adjustment** | [**DateAdjustment**](DateAdjustment.md) |  | 
**time_adjustment** | [**TimeAdjustment**](TimeAdjustment.md) |  | 
## Example

```python
from lusid_workflow.models.scheduled_time_adjustment import ScheduledTimeAdjustment
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

date_adjustment: DateAdjustment = # Replace with your value
time_adjustment: TimeAdjustment = # Replace with your value
scheduled_time_adjustment_instance = ScheduledTimeAdjustment(date_adjustment=date_adjustment, time_adjustment=time_adjustment)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

