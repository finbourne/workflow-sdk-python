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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Optional[List[Task]] = # Replace with your value
failed: Optional[List[ErrorDetail]] = # Replace with your value
links: Optional[List[Link]] = None
batch_update_tasks_response_instance = BatchUpdateTasksResponse(values=values, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

