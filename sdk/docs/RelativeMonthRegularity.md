# RelativeMonthRegularity

Relative Month Regularity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | The frequency of the Relative Month Regularity | 
**days_of_week** | **List[str]** | Days of the week | 
**index** | **str** | Relative index in the month | 
**type** | **str** | The type of Date Regularity | 
## Example

```python
from lusid_workflow.models.relative_month_regularity import RelativeMonthRegularity
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conint, conlist, constr

frequency: conint(strict=True, le=100, ge=1) = Field(..., description="The frequency of the Relative Month Regularity")
frequency: StrictInt = 42
days_of_week: conlist(StrictStr, max_items=7, min_items=1) = Field(..., alias="daysOfWeek", description="Days of the week")
index: StrictStr = "example_index"
type: StrictStr = "example_type"
relative_month_regularity_instance = RelativeMonthRegularity(frequency=frequency, days_of_week=days_of_week, index=index, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

