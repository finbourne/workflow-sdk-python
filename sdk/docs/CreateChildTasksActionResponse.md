# CreateChildTasksActionResponse

Defines a read-only Create Child Tasks Action
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | [optional] 
**child_task_configurations** | [**List[CreateChildTaskConfiguration]**](CreateChildTaskConfiguration.md) | The Child Task Configurations | [optional] 
**ordering** | **str** | How the created child tasks are ordered for execution: Parallel (default) or Series. In Series the child tasks form a chain and only the first is started; each later one is started by its predecessor&#39;s TriggerNextTask action, or by another trigger such as a TriggerChildTasks filter on previousTask. Without one, the chain stops after the first child. | [optional] 
## Example

```python
from lusid_workflow.models.create_child_tasks_action_response import CreateChildTasksActionResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
child_task_configurations: Optional[List[CreateChildTaskConfiguration]] = # Replace with your value
ordering: Optional[StrictStr] = "example_ordering"
create_child_tasks_action_response_instance = CreateChildTasksActionResponse(type=type, child_task_configurations=child_task_configurations, ordering=ordering)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

