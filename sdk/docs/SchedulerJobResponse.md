# SchedulerJobResponse

Readonly configuration for a Worker that calls a Scheduler job
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | [optional] 
**job_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid_workflow.models.scheduler_job_response import SchedulerJobResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
job_id: Optional[ResourceId] = # Replace with your value
scheduler_job_response_instance = SchedulerJobResponse(type=type, job_id=job_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

