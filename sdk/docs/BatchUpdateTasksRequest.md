# BatchUpdateTasksRequest

A request to update multiple Tasks
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_tasks** | [**List[UpdateTaskWithIdAndTriggerRequest]**](UpdateTaskWithIdAndTriggerRequest.md) | A Dictionary of task IDs to UpdateTaskRequest | [optional] 
## Example

```python
from lusid_workflow.models.batch_update_tasks_request import BatchUpdateTasksRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

update_tasks: Optional[List[UpdateTaskWithIdAndTriggerRequest]] = # Replace with your value
batch_update_tasks_request_instance = BatchUpdateTasksRequest(update_tasks=update_tasks)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

