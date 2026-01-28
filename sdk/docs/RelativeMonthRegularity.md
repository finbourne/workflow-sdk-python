# RelativeMonthRegularity

Relative Month Regularity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | The frequency of the Relative Month Regularity. For example, a value of 2 indicates every 2 months | 
**days_of_week** | **List[str]** | Days of the week. One or more of - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday | 
**index** | **str** | Relative index in the month. One of - First, Second, Third, Fourth, Last. For example, to specify the second Tuesday of every month, set DaysOfWeek to [\&quot;Tuesday\&quot;] and Index to \&quot;Second\&quot; | 
**type** | **str** | The type of Date Regularity | 
## Example

```python
from lusid_workflow.models.relative_month_regularity import RelativeMonthRegularity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

frequency: StrictInt = # Replace with your value
frequency: StrictInt = 42
days_of_week: List[StrictStr] = # Replace with your value
index: StrictStr = "example_index"
type: StrictStr = "example_type"
relative_month_regularity_instance = RelativeMonthRegularity(frequency=frequency, days_of_week=days_of_week, index=index, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

