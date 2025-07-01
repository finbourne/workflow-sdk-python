# ScheduleMatchingPattern

The Schedule Matching Pattern to trigger on
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ScheduleMatchingPatternContext**](ScheduleMatchingPatternContext.md) |  | 
**recurrence_pattern** | [**RecurrencePattern**](RecurrencePattern.md) |  | 
## Example

```python
from lusid_workflow.models.schedule_matching_pattern import ScheduleMatchingPattern
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

context: ScheduleMatchingPatternContext = # Replace with your value
recurrence_pattern: RecurrencePattern = # Replace with your value
schedule_matching_pattern_instance = ScheduleMatchingPattern(context=context, recurrence_pattern=recurrence_pattern)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

