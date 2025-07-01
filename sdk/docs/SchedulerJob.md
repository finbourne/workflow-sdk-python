# SchedulerJob

Configuration for a Worker that calls a Scheduler Job
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | 
**job_id** | [**ResourceId**](ResourceId.md) |  | 
## Example

```python
from lusid_workflow.models.scheduler_job import SchedulerJob
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

type: StrictStr = "example_type"
job_id: ResourceId = # Replace with your value
scheduler_job_instance = SchedulerJob(type=type, job_id=job_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

