# DateAdjustment

A date adjustment to apply to the scheduled time of an EventHandler with a Finbourne.Workflow.WebApi.Common.Dto.Json.EventHandlers.ScheduleMatchingPattern
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta_days** | **int** | The delta to apply to the date part of the scheduled time, in days | 
**business_day_adjustment** | **str** | The Business Day Adjustment | 
## Example

```python
from lusid_workflow.models.date_adjustment import DateAdjustment
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

delta_days: StrictInt = # Replace with your value
delta_days: StrictInt = 42
business_day_adjustment: StrictStr = "example_business_day_adjustment"
date_adjustment_instance = DateAdjustment(delta_days=delta_days, business_day_adjustment=business_day_adjustment)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

