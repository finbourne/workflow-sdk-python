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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

month: StrictInt = # Replace with your value
month: StrictInt = 42
day: StrictInt = # Replace with your value
day: StrictInt = 42
day_of_year_instance = DayOfYear(month=month, day=day)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

