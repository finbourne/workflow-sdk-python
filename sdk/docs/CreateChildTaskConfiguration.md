# CreateChildTaskConfiguration

Create Child Task Configuration
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**task_definition_as_at** | **datetime** | TaskDefinition AsAt timestamp | [optional] 
**initial_trigger** | **str** | The Initial Trigger for automatic start | [optional] 
**child_task_fields** | [**Dict[str, FieldMapping]**](FieldMapping.md) | Field Mappings | [optional] 
**map_stacking_key_from** | **str** | If present, the value of this field on the parent task will be the Stacking Key on any created child tasks | [optional] 
## Example

```python
from lusid_workflow.models.create_child_task_configuration import CreateChildTaskConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

task_definition_id: ResourceId = # Replace with your value
task_definition_as_at: Optional[datetime] = # Replace with your value
initial_trigger: Optional[StrictStr] = "example_initial_trigger"
child_task_fields: Optional[Dict[str, FieldMapping]] = # Replace with your value
map_stacking_key_from: Optional[StrictStr] = "example_map_stacking_key_from"
create_child_task_configuration_instance = CreateChildTaskConfiguration(task_definition_id=task_definition_id, task_definition_as_at=task_definition_as_at, initial_trigger=initial_trigger, child_task_fields=child_task_fields, map_stacking_key_from=map_stacking_key_from)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

