# WorkerStatusTriggers

Defines triggers that will be invoked per Worker outcome
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started** | **str** | Trigger to invoke when the Worker has Started | [optional] 
**completed_with_results** | **str** | Trigger to invoke when the Worker has Completed (with results) | [optional] 
**completed_no_results** | **str** | Trigger to invoke when the Worker has Completed (no results) | [optional] 
**failed_to_start** | **str** | Trigger to invoke when the Worker has Failed to Start | [optional] 
**failed_to_complete** | **str** | Trigger to invoke when the Worker has Failed to Complete | [optional] 
## Example

```python
from lusid_workflow.models.worker_status_triggers import WorkerStatusTriggers
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

started: Optional[StrictStr] = "example_started"
completed_with_results: Optional[StrictStr] = "example_completed_with_results"
completed_no_results: Optional[StrictStr] = "example_completed_no_results"
failed_to_start: Optional[StrictStr] = "example_failed_to_start"
failed_to_complete: Optional[StrictStr] = "example_failed_to_complete"
worker_status_triggers_instance = WorkerStatusTriggers(started=started, completed_with_results=completed_with_results, completed_no_results=completed_no_results, failed_to_start=failed_to_start, failed_to_complete=failed_to_complete)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

