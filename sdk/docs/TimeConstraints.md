# TimeConstraints

Time constraints for a Recurrence Pattern
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Start date of the Recurrence Pattern | 
**end_date** | **str** | Optional end date of the Recurrence Pattern | [optional] 
**times_of_day** | [**List[TimeOfDay]**](TimeOfDay.md) | Times of the day to run the Recurrence Pattern | 
## Example

```python
from lusid_workflow.models.time_constraints import TimeConstraints
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

start_date: StrictStr = "example_start_date"
end_date: Optional[StrictStr] = "example_end_date"
times_of_day: conlist(TimeOfDay, max_items=5, min_items=1) = Field(..., alias="timesOfDay", description="Times of the day to run the Recurrence Pattern")
time_constraints_instance = TimeConstraints(start_date=start_date, end_date=end_date, times_of_day=times_of_day)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

