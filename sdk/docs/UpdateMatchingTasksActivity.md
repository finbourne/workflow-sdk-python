# UpdateMatchingTasksActivity

Update all matching tasks based on filter matches
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of task activity | 
**filter** | **str** | The filter that matches on existing tasks | [optional] 
**trigger** | **str** | Trigger to supply to all tasks that have been matched | 
**correlation_ids** | [**List[EventHandlerMapping]**](EventHandlerMapping.md) | The event to correlation ID mappings | [optional] 
**task_fields** | [**Dict[str, FieldMapping]**](FieldMapping.md) | The event to task field mappings | [optional] 
**schedule_dependent_task_fields** | [**Dict[str, ScheduledTimeAdjustment]**](ScheduledTimeAdjustment.md) | The Schedule dependent task field mappings. Only relevant if a Finbourne.Workflow.WebApi.Common.Dto.Json.EventHandlers.ScheduleMatchingPattern is specified | [optional] 
## Example

```python
from lusid_workflow.models.update_matching_tasks_activity import UpdateMatchingTasksActivity
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

type: StrictStr = "example_type"
filter: Optional[StrictStr] = "example_filter"
trigger: StrictStr = "example_trigger"
correlation_ids: Optional[conlist(EventHandlerMapping)] = # Replace with your value
task_fields: Optional[Dict[str, FieldMapping]] = # Replace with your value
schedule_dependent_task_fields: Optional[Dict[str, ScheduledTimeAdjustment]] = # Replace with your value
update_matching_tasks_activity_instance = UpdateMatchingTasksActivity(type=type, filter=filter, trigger=trigger, correlation_ids=correlation_ids, task_fields=task_fields, schedule_dependent_task_fields=schedule_dependent_task_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

