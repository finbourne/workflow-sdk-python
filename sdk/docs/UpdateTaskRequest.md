# UpdateTaskRequest

A request to update a Task
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_ids** | **List[str]** | A set of guid identifiers that allow correlation across the application tier | [optional] 
**fields** | [**List[TaskInstanceField]**](TaskInstanceField.md) | Defines the fields associated with the update | [optional] 
**stacking_key** | **str** | The key for the Stack that this Task should be added to | [optional] 
## Example

```python
from lusid_workflow.models.update_task_request import UpdateTaskRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

correlation_ids: Optional[conlist(StrictStr)] = # Replace with your value
fields: Optional[conlist(TaskInstanceField)] = # Replace with your value
stacking_key: Optional[StrictStr] = "example_stacking_key"
update_task_request_instance = UpdateTaskRequest(correlation_ids=correlation_ids, fields=fields, stacking_key=stacking_key)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

