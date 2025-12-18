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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

hours: StrictInt = # Replace with your value
hours: StrictInt = 42
minutes: StrictInt = # Replace with your value
minutes: StrictInt = 42
type: StrictStr = "example_type"
specified_time_instance = SpecifiedTime(hours=hours, minutes=minutes, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

