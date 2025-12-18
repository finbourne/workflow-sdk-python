# CreateNewTaskActivityResponse

Read only Create new task response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of task activity | [optional] 
**initial_trigger** | **str** | Trigger to supply to all tasks to be made | [optional] 
**correlation_ids** | [**List[EventHandlerMapping]**](EventHandlerMapping.md) | The event to correlation ID mappings | [optional] 
**task_fields** | [**Dict[str, FieldMapping]**](FieldMapping.md) | The event to task field mappings | [optional] 
**schedule_dependent_task_fields** | [**Dict[str, ScheduledTimeAdjustment]**](ScheduledTimeAdjustment.md) | The Schedule dependent task field mappings. Only relevant if a Finbourne.Workflow.WebApi.Common.Dto.Json.EventHandlers.ScheduleMatchingPattern is specified | [optional] 
## Example

```python
from lusid_workflow.models.create_new_task_activity_response import CreateNewTaskActivityResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
initial_trigger: Optional[StrictStr] = "example_initial_trigger"
correlation_ids: Optional[List[EventHandlerMapping]] = # Replace with your value
task_fields: Optional[Dict[str, FieldMapping]] = # Replace with your value
schedule_dependent_task_fields: Optional[Dict[str, ScheduledTimeAdjustment]] = # Replace with your value
create_new_task_activity_response_instance = CreateNewTaskActivityResponse(type=type, initial_trigger=initial_trigger, correlation_ids=correlation_ids, task_fields=task_fields, schedule_dependent_task_fields=schedule_dependent_task_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

