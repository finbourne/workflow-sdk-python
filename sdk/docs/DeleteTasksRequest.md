# DeleteTasksRequest

Contains required info to delete Tasks
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_ids** | **List[str]** | The Ids of the Tasks to delete | [optional] 
## Example

```python
from lusid_workflow.models.delete_tasks_request import DeleteTasksRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

task_ids: Optional[List[StrictStr]] = # Replace with your value
delete_tasks_request_instance = DeleteTasksRequest(task_ids=task_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

