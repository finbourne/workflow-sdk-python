# BatchUpdateTasksRequest

A request to update multiple Tasks
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_tasks** | [**List[UpdateTaskWithIdAndTriggerRequest]**](UpdateTaskWithIdAndTriggerRequest.md) | A Dictionary of task IDs to UpdateTaskRequest | [optional] 
## Example

```python
from lusid_workflow.models.batch_update_tasks_request import BatchUpdateTasksRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

update_tasks: Optional[conlist(UpdateTaskWithIdAndTriggerRequest)] = # Replace with your value
batch_update_tasks_request_instance = BatchUpdateTasksRequest(update_tasks=update_tasks)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

