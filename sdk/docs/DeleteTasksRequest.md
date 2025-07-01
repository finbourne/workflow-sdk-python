# DeleteTasksRequest

Contains required info to delete Tasks
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_ids** | **List[str]** | The Ids of the Tasks to delete | [optional] 
## Example

```python
from lusid_workflow.models.delete_tasks_request import DeleteTasksRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

task_ids: Optional[conlist(StrictStr)] = # Replace with your value
delete_tasks_request_instance = DeleteTasksRequest(task_ids=task_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

