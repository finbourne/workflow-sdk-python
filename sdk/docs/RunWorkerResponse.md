# RunWorkerResponse

The RunWorker response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | Identifies a Worker run | 
**status_detail** | **str** | Detail on the final status | [optional] 
## Example

```python
from lusid_workflow.models.run_worker_response import RunWorkerResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: StrictStr = "example_run_id"
status_detail: Optional[StrictStr] = "example_status_detail"
run_worker_response_instance = RunWorkerResponse(run_id=run_id, status_detail=status_detail)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

