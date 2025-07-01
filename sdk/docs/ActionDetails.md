# ActionDetails

Abstracts the kinds of Actions available
## Example

```python
from lusid_workflow.models.action_details import ActionDetails
from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator

# Example with ActionDetails 

create_child_tasks_action_instance = lusid_workflow.models.create_child_tasks_action.CreateChildTasksAction(
                        type = 'CreateChildTasks', 
                        child_task_configurations = [
                            lusid_workflow.models.create_child_task_configuration.CreateChildTaskConfiguration(
                                task_definition_id = lusid_workflow.models.resource_id.ResourceId(
                                    scope = '', 
                                    code = '', ), 
                                task_definition_as_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                initial_trigger = 'z', 
                                child_task_fields = {
                                    'key' : lusid_workflow.models.field_mapping.FieldMapping(
                                        map_from = '0', 
                                        set_to = null, )
                                    }, 
                                map_stacking_key_from = '', )
                            ], )

action_details_instance = ActionDetails(create_child_tasks_action_instance)

```
See all compatible oneOf types with ActionDetails


 * [RunWorkerAction](./RunWorkerAction.md)

 * [TriggerParentTaskAction](./TriggerParentTaskAction.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

