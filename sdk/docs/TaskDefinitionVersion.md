# TaskDefinitionVersion

The version of the Task Definition used by this Task
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_modified** | **datetime** | The asAt datetime of the Task Definition used by this Task | [optional] 
## Example

```python
from lusid_workflow.models.task_definition_version import TaskDefinitionVersion
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at_modified: Optional[datetime] = # Replace with your value
task_definition_version_instance = TaskDefinitionVersion(as_at_modified=as_at_modified)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

