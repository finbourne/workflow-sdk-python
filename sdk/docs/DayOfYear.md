# DayOfYear

A day in the year
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **int** | Month in the year | 
**day** | **int** | Day in the month | 
## Example

```python
from lusid_workflow.models.day_of_year import DayOfYear
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, conint

month: conint(strict=True, le=12, ge=1) = Field(..., description="Month in the year")
month: StrictInt = 42
day: conint(strict=True, le=31, ge=1) = Field(..., description="Day in the month")
day: StrictInt = 42
day_of_year_instance = DayOfYear(month=month, day=day)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

