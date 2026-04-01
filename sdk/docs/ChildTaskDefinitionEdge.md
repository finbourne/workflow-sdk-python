# ChildTaskDefinitionEdge

Represents a parent-child relationship between two Task Definitions in a Workflow
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**VersionedTaskDefinitionId**](VersionedTaskDefinitionId.md) |  | [optional] 
**child** | [**VersionedTaskDefinitionId**](VersionedTaskDefinitionId.md) |  | [optional] 
## Example

```python
from lusid_workflow.models.child_task_definition_edge import ChildTaskDefinitionEdge
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

parent: Optional[VersionedTaskDefinitionId] = None
child: Optional[VersionedTaskDefinitionId] = None
child_task_definition_edge_instance = ChildTaskDefinitionEdge(parent=parent, child=child)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

