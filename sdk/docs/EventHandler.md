# EventHandler

Information about an Event Handler
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**version** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**status** | **str** | The current status of the event handler | 
**event_matching_pattern** | [**EventMatchingPattern**](EventMatchingPattern.md) |  | [optional] 
**schedule_matching_pattern** | [**ScheduleMatchingPattern**](ScheduleMatchingPattern.md) |  | [optional] 
**run_as_user_id** | [**EventHandlerMapping**](EventHandlerMapping.md) |  | 
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**task_definition_as_at** | **datetime** | AsAt of the required task definition | [optional] 
**task_activity** | [**TaskActivityResponse**](TaskActivityResponse.md) |  | 
## Example

```python
from lusid_workflow.models.event_handler import EventHandler
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
version: Optional[VersionInfo] = None
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
status: StrictStr = "example_status"
event_matching_pattern: Optional[EventMatchingPattern] = # Replace with your value
schedule_matching_pattern: Optional[ScheduleMatchingPattern] = # Replace with your value
run_as_user_id: EventHandlerMapping = # Replace with your value
task_definition_id: ResourceId = # Replace with your value
task_definition_as_at: Optional[datetime] = # Replace with your value
task_activity: TaskActivityResponse = # Replace with your value
event_handler_instance = EventHandler(id=id, version=version, display_name=display_name, description=description, status=status, event_matching_pattern=event_matching_pattern, schedule_matching_pattern=schedule_matching_pattern, run_as_user_id=run_as_user_id, task_definition_id=task_definition_id, task_definition_as_at=task_definition_as_at, task_activity=task_activity)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

