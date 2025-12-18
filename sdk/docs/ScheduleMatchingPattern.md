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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

context: ScheduleMatchingPatternContext
recurrence_pattern: RecurrencePattern = # Replace with your value
schedule_matching_pattern_instance = ScheduleMatchingPattern(context=context, recurrence_pattern=recurrence_pattern)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

