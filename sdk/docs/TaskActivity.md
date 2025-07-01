# TaskActivity

Information about what tasks to create/update when receiving events
## Example

```python
from lusid_workflow.models.task_activity import TaskActivity
from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator

# Example with TaskActivity 

create_new_task_activity_instance = lusid_workflow.models.create_new_task_activity.CreateNewTaskActivity(
                        initial_trigger = '', 
                        type = 'CreateNewTask', 
                        correlation_ids = [
                            lusid_workflow.models.event_handler_mapping.EventHandlerMapping(
                                map_from = '', 
                                set_to = '', )
                            ], 
                        task_fields = {
                            'key' : lusid_workflow.models.field_mapping.FieldMapping(
                                map_from = '0', 
                                set_to = null, )
                            }, )

task_activity_instance = TaskActivity(create_new_task_activity_instance)

```
See all compatible oneOf types with TaskActivity


 * [UpdateMatchingTasksActivity](./UpdateMatchingTasksActivity.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

