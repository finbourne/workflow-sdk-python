# ScheduleTaskFieldMapping

How a Schedule Launcher fills one field of the root task from the instant the schedule fired
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map_from** | **str** | The value the field is taken from. One of - ScheduledTime | 
**date_time_adjustment** | [**DateTimeAdjustment**](DateTimeAdjustment.md) |  | [optional] 
## Example

```python
from lusid_workflow.models.schedule_task_field_mapping import ScheduleTaskFieldMapping
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

map_from: StrictStr = "example_map_from"
date_time_adjustment: Optional[DateTimeAdjustment] = # Replace with your value
schedule_task_field_mapping_instance = ScheduleTaskFieldMapping(map_from=map_from, date_time_adjustment=date_time_adjustment)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

