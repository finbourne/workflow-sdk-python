# WorkflowStructureNodes

The nodes of a Workflow structure graph — the Task Definitions and the Launchers involved
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_definitions** | [**List[TaskDefinition]**](TaskDefinition.md) | The Task Definitions that make up the nodes of this Workflow | [optional] 
**launchers** | [**List[LauncherResponse]**](LauncherResponse.md) | The Launchers of this Workflow, as full Launcher objects. At most the first 10 by launcher id are returned, in the same order as ListLaunchers gives by default. Inactive Launchers are included. When the Workflow has more, launchersTruncated is true and ListLaunchers returns the full set | [optional] 
## Example

```python
from lusid_workflow.models.workflow_structure_nodes import WorkflowStructureNodes
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

task_definitions: Optional[List[TaskDefinition]] = # Replace with your value
launchers: Optional[List[LauncherResponse]] = # Replace with your value
workflow_structure_nodes_instance = WorkflowStructureNodes(task_definitions=task_definitions, launchers=launchers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

