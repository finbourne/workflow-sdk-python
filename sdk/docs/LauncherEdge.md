# LauncherEdge

Represents the relationship between a Launcher of a Workflow and the Task Definition it starts a run of
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**launcher_id** | **str** | The identifier of the Launcher inside its Workflow | [optional] 
**target_task_definition** | [**VersionedTaskDefinitionId**](VersionedTaskDefinitionId.md) |  | [optional] 
## Example

```python
from lusid_workflow.models.launcher_edge import LauncherEdge
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

launcher_id: Optional[StrictStr] = "example_launcher_id"
target_task_definition: Optional[VersionedTaskDefinitionId] = # Replace with your value
launcher_edge_instance = LauncherEdge(launcher_id=launcher_id, target_task_definition=target_task_definition)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

