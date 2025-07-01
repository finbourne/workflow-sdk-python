# BatchUpdateTasksResponse

Defines a representation of tasks that have been updated
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Task]**](Task.md) | Successful tasks brought back from the BatchUpdate call | [optional] [readonly] 
**failed** | [**List[ErrorDetail]**](ErrorDetail.md) | Individual failures for each task returned from the BatchUpdate call | [optional] [readonly] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid_workflow.models.batch_update_tasks_response import BatchUpdateTasksResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

values: Optional[conlist(Task)] = # Replace with your value
failed: Optional[conlist(ErrorDetail)] = # Replace with your value
links: Optional[conlist(Link)] = None
batch_update_tasks_response_instance = BatchUpdateTasksResponse(values=values, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

