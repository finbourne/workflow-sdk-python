# GetWorkerResultResponse

The RunWorker response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**worker_status** | **str** | The final status of the Worker | 
**results** | **List[Dict[str, object]]** | Results | 
**status_detail** | **str** | Detail on the final status | [optional] 
## Example

```python
from lusid_workflow.models.get_worker_result_response import GetWorkerResultResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

worker_status: StrictStr = "example_worker_status"
results: List[Dict[str, Any]] = # Replace with your value
status_detail: Optional[StrictStr] = "example_status_detail"
get_worker_result_response_instance = GetWorkerResultResponse(worker_status=worker_status, results=results, status_detail=status_detail)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

