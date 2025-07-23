# TimeAdjustment

A time adjustment to apply to the scheduled time of an EventHandler with a Finbourne.Workflow.WebApi.Common.Dto.Json.EventHandlers.ScheduleMatchingPattern
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set_to** | [**SpecifiedTime**](SpecifiedTime.md) |  | 
## Example

```python
from lusid_workflow.models.time_adjustment import TimeAdjustment
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

set_to: SpecifiedTime = # Replace with your value
time_adjustment_instance = TimeAdjustment(set_to=set_to)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

