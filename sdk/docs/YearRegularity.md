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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

dates: List[DayOfYear] = # Replace with your value
type: StrictStr = "example_type"
year_regularity_instance = YearRegularity(dates=dates, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

