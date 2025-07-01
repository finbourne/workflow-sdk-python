# ActionDetailsResponse

Abstracts the kinds of Actions available in a read-only form
## Example

```python
from lusid_workflow.models.action_details_response import ActionDetailsResponse
from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator

# Example with ActionDetailsResponse 

create_child_tasks_action_response_instance = lusid_workflow.models.create_child_tasks_action_response.CreateChildTasksActionResponse(
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

action_details_response_instance = ActionDetailsResponse(create_child_tasks_action_response_instance)

```
See all compatible oneOf types with ActionDetailsResponse


 * [RunWorkerActionResponse](./RunWorkerActionResponse.md)

 * [TriggerParentTaskActionResponse](./TriggerParentTaskActionResponse.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

