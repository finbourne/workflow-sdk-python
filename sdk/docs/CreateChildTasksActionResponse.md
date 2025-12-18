# CreateChildTasksActionResponse

Defines a read-only Create Child Tasks Action
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | [optional] 
**child_task_configurations** | [**List[CreateChildTaskConfiguration]**](CreateChildTaskConfiguration.md) | The Child Task Configurations | [optional] 
## Example

```python
from lusid_workflow.models.create_child_tasks_action_response import CreateChildTasksActionResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
child_task_configurations: Optional[List[CreateChildTaskConfiguration]] = # Replace with your value
create_child_tasks_action_response_instance = CreateChildTasksActionResponse(type=type, child_task_configurations=child_task_configurations)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

