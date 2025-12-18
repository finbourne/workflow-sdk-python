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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

frequency: StrictInt = # Replace with your value
frequency: StrictInt = 42
type: StrictStr = "example_type"
day_regularity_instance = DayRegularity(frequency=frequency, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

