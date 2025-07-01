# YearRegularity

Year Regularity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dates** | [**List[DayOfYear]**](DayOfYear.md) | The dates in the year | 
**type** | **str** | The type of Date Regularity | 
## Example

```python
from lusid_workflow.models.year_regularity import YearRegularity
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr

dates: conlist(DayOfYear, max_items=366, min_items=1) = Field(..., description="The dates in the year")
type: StrictStr = "example_type"
year_regularity_instance = YearRegularity(dates=dates, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

