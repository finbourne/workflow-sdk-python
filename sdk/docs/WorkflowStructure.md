# WorkflowStructure

Describes the structure of a Workflow as a graph of its Task Definitions and its Launchers
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**WorkflowStructureNodes**](WorkflowStructureNodes.md) |  | [optional] 
**edges** | [**WorkflowStructureEdges**](WorkflowStructureEdges.md) |  | [optional] 
**launchers_truncated** | **bool** | True when the Workflow has more Launchers than were returned inline in nodes.launchers. Call ListLaunchers for the full set | [optional] 
## Example

```python
from lusid_workflow.models.workflow_structure import WorkflowStructure
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

nodes: Optional[WorkflowStructureNodes] = None
edges: Optional[WorkflowStructureEdges] = None
launchers_truncated: Optional[StrictBool] = # Replace with your value
launchers_truncated:Optional[StrictBool] = None
workflow_structure_instance = WorkflowStructure(nodes=nodes, edges=edges, launchers_truncated=launchers_truncated)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

