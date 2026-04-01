# VersionedTaskDefinitionId

A Task Definition Id with an optional asAt timestamp identifying a specific version
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**task_definition_as_at** | **datetime** | The asAt time of this version of the Task Definition. Null means the latest version. | [optional] 
## Example

```python
from lusid_workflow.models.versioned_task_definition_id import VersionedTaskDefinitionId
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

task_definition_id: Optional[ResourceId] = # Replace with your value
task_definition_as_at: Optional[datetime] = # Replace with your value
versioned_task_definition_id_instance = VersionedTaskDefinitionId(task_definition_id=task_definition_id, task_definition_as_at=task_definition_as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

