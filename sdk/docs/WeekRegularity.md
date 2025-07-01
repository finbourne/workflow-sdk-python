# WeekRegularity

Week Regularity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | The frequency of the Week Regularity | 
**days_of_week** | **List[str]** | Days of the week | 
**type** | **str** | The type of Date Regularity | 
## Example

```python
from lusid_workflow.models.week_regularity import WeekRegularity
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conint, conlist, constr

frequency: conint(strict=True, le=100, ge=1) = Field(..., description="The frequency of the Week Regularity")
frequency: StrictInt = 42
days_of_week: conlist(StrictStr, max_items=7, min_items=1) = Field(..., alias="daysOfWeek", description="Days of the week")
type: StrictStr = "example_type"
week_regularity_instance = WeekRegularity(frequency=frequency, days_of_week=days_of_week, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

