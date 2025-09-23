# CreateNewTaskActivity

Define a Task Activity that creates a new task
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_trigger** | **str** | Trigger to supply to all tasks to be made | [optional] 
**type** | **str** | The type of task activity | 
**correlation_ids** | [**List[EventHandlerMapping]**](EventHandlerMapping.md) | The event to correlation ID mappings | [optional] 
**task_fields** | [**Dict[str, FieldMapping]**](FieldMapping.md) | The event to task field mappings | [optional] 
**schedule_dependent_task_fields** | [**Dict[str, ScheduledTimeAdjustment]**](ScheduledTimeAdjustment.md) | The Schedule dependent task field mappings. Only relevant if a Finbourne.Workflow.WebApi.Common.Dto.Json.EventHandlers.ScheduleMatchingPattern is specified | [optional] 
## Example

```python
from lusid_workflow.models.create_new_task_activity import CreateNewTaskActivity
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

initial_trigger: Optional[StrictStr] = "example_initial_trigger"
type: StrictStr = "example_type"
correlation_ids: Optional[conlist(EventHandlerMapping)] = # Replace with your value
task_fields: Optional[Dict[str, FieldMapping]] = # Replace with your value
schedule_dependent_task_fields: Optional[Dict[str, ScheduledTimeAdjustment]] = # Replace with your value
create_new_task_activity_instance = CreateNewTaskActivity(initial_trigger=initial_trigger, type=type, correlation_ids=correlation_ids, task_fields=task_fields, schedule_dependent_task_fields=schedule_dependent_task_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

