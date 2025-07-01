# RecurrencePattern

The Recurrence Pattern
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_constraints** | [**TimeConstraints**](TimeConstraints.md) |  | 
**date_regularity** | [**DateRegularity**](DateRegularity.md) |  | 
**business_day_adjustment** | **str** | The Business Day Adjustment | 
## Example

```python
from lusid_workflow.models.recurrence_pattern import RecurrencePattern
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

time_constraints: TimeConstraints = # Replace with your value
date_regularity: DateRegularity = # Replace with your value
business_day_adjustment: StrictStr = "example_business_day_adjustment"
recurrence_pattern_instance = RecurrencePattern(time_constraints=time_constraints, date_regularity=date_regularity, business_day_adjustment=business_day_adjustment)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

