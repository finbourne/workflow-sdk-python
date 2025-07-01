# DayRegularity

Day Regularity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | The frequency of the Day Regularity | 
**type** | **str** | The type of Date Regularity | 
## Example

```python
from lusid_workflow.models.day_regularity import DayRegularity
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, conint, constr

frequency: conint(strict=True, le=1000, ge=1) = Field(..., description="The frequency of the Day Regularity")
frequency: StrictInt = 42
type: StrictStr = "example_type"
day_regularity_instance = DayRegularity(frequency=frequency, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

