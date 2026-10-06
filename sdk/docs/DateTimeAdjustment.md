# DateTimeAdjustment

A change applied to the date and the time of a source value, in a named calendar context.              At least one of Finbourne.Workflow.WebApi.Common.Dto.Json.Launchers.DateTimeAdjustment.DateAdjustment or Finbourne.Workflow.WebApi.Common.Dto.Json.Launchers.DateTimeAdjustment.TimeAdjustment must be given
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_context** | **str** | The name of the calendar context this change happens in, which must be one the Launcher declares. When it is left out a Schedule Launcher uses the context of its schedule | [optional] 
**date_adjustment** | [**DateAdjustment**](DateAdjustment.md) |  | [optional] 
**time_adjustment** | [**TimeAdjustment**](TimeAdjustment.md) |  | [optional] 
## Example

```python
from lusid_workflow.models.date_time_adjustment import DateTimeAdjustment
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

calendar_context: Optional[StrictStr] = "example_calendar_context"
date_adjustment: Optional[DateAdjustment] = # Replace with your value
time_adjustment: Optional[TimeAdjustment] = # Replace with your value
date_time_adjustment_instance = DateTimeAdjustment(calendar_context=calendar_context, date_adjustment=date_adjustment, time_adjustment=time_adjustment)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

