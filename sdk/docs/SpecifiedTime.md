# SpecifiedTime

A specified time in the day
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hours** | **int** | Hours | 
**minutes** | **int** | Minutes | 
**type** | **str** | The type of Time of Day | 
## Example

```python
from lusid_workflow.models.specified_time import SpecifiedTime
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, conint, constr

hours: conint(strict=True, le=23, ge=0) = Field(..., description="Hours")
hours: StrictInt = 42
minutes: conint(strict=True, le=59, ge=0) = Field(..., description="Minutes")
minutes: StrictInt = 42
type: StrictStr = "example_type"
specified_time_instance = SpecifiedTime(hours=hours, minutes=minutes, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

