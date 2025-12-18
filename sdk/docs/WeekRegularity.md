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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

frequency: StrictInt = # Replace with your value
frequency: StrictInt = 42
days_of_week: List[StrictStr] = # Replace with your value
type: StrictStr = "example_type"
week_regularity_instance = WeekRegularity(frequency=frequency, days_of_week=days_of_week, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

