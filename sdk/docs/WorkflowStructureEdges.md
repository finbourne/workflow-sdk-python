# WorkflowStructureEdges

The edges of a Workflow structure graph — the parent-child relationships between Task Definitions and the relationships between Launchers and the Task Definitions they start
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_task_definitions** | [**List[ChildTaskDefinitionEdge]**](ChildTaskDefinitionEdge.md) | The child Task Definition relationships | [optional] 
**launchers** | [**List[LauncherEdge]**](LauncherEdge.md) | The Launcher relationships. There is one entry per Launcher in nodes.launchers, in the same order | [optional] 
## Example

```python
from lusid_workflow.models.workflow_structure_edges import WorkflowStructureEdges
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

child_task_definitions: Optional[List[ChildTaskDefinitionEdge]] = # Replace with your value
launchers: Optional[List[LauncherEdge]] = # Replace with your value
workflow_structure_edges_instance = WorkflowStructureEdges(child_task_definitions=child_task_definitions, launchers=launchers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

