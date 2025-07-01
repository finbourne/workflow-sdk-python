# SpecificMonthRegularity

Specific Month Regularity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | The frequency of the Specific Month Regularity | 
**days_of_month** | **List[int]** | Days of the month | 
**type** | **str** | The type of Date Regularity | 
## Example

```python
from lusid_workflow.models.specific_month_regularity import SpecificMonthRegularity
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictInt, conint, conlist, constr

frequency: conint(strict=True, le=100, ge=1) = Field(..., description="The frequency of the Specific Month Regularity")
frequency: StrictInt = 42
days_of_month: conlist(StrictInt, max_items=31, min_items=1) = Field(..., alias="daysOfMonth", description="Days of the month")
type: StrictStr = "example_type"
specific_month_regularity_instance = SpecificMonthRegularity(frequency=frequency, days_of_month=days_of_month, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

