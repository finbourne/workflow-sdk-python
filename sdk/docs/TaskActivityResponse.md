# TaskActivityResponse

Readonly information about how the worker should be executed
## Example

```python
from lusid_workflow.models.task_activity_response import TaskActivityResponse
from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator

# Example with TaskActivityResponse 

create_new_task_activity_response_instance = lusid_workflow.models.create_new_task_activity_response.CreateNewTaskActivityResponse(
                        type = 'CreateNewTask', 
                        initial_trigger = '', 
                        correlation_ids = [
                            lusid_workflow.models.event_handler_mapping.EventHandlerMapping(
                                map_from = '', 
                                set_to = '', )
                            ], 
                        task_fields = {
                            'key' : lusid_workflow.models.field_mapping.FieldMapping(
                                map_from = '0', 
                                set_to = null, )
                            }, 
                        schedule_dependent_task_fields = {
                            'key' : lusid_workflow.models.scheduled_time_adjustment.ScheduledTimeAdjustment(
                                date_adjustment = lusid_workflow.models.date_adjustment.DateAdjustment(
                                    delta_days = -10000, 
                                    business_day_adjustment = '0', ), 
                                time_adjustment = lusid_workflow.models.time_adjustment.TimeAdjustment(
                                    set_to = lusid_workflow.models.specified_time.SpecifiedTime(
                                        hours = 0, 
                                        minutes = 0, 
                                        type = '0', ), ), )
                            }, )

task_activity_response_instance = TaskActivityResponse(create_new_task_activity_response_instance)

```
See all compatible oneOf types with TaskActivityResponse


 * [UpdateMatchingTasksActivityResponse](./UpdateMatchingTasksActivityResponse.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

