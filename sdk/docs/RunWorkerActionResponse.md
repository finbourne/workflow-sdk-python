# RunWorkerActionResponse

Defines a read-only Run Worker Action
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | [optional] 
**worker_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**worker_as_at** | **datetime** | Worker AsAt | [optional] 
**worker_parameters** | [**Dict[str, FieldMapping]**](FieldMapping.md) | Parameters for this Worker | [optional] 
**worker_status_triggers** | [**WorkerStatusTriggers**](WorkerStatusTriggers.md) |  | [optional] 
**child_task_configurations** | [**List[ResultantChildTaskConfiguration]**](ResultantChildTaskConfiguration.md) | Tasks can be generated from run worker results; this is the configuration | [optional] 
**re_run_configurations** | [**List[ReRunConfiguration]**](ReRunConfiguration.md) | Configuration governing how re-run results are reconciled against existing child tasks from a previous run of this action against the same parent Task instance | [optional] 
**worker_timeout** | **int** | Worker timeout in seconds | [optional] 
**ordering** | **str** | How the created child tasks are ordered for execution: Parallel (default), Series, or ParallelSeries | [optional] 
## Example

```python
from lusid_workflow.models.run_worker_action_response import RunWorkerActionResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
worker_id: Optional[ResourceId] = # Replace with your value
worker_as_at: Optional[datetime] = # Replace with your value
worker_parameters: Optional[Dict[str, FieldMapping]] = # Replace with your value
worker_status_triggers: Optional[WorkerStatusTriggers] = # Replace with your value
child_task_configurations: Optional[List[ResultantChildTaskConfiguration]] = # Replace with your value
re_run_configurations: Optional[List[ReRunConfiguration]] = # Replace with your value
worker_timeout: Optional[StrictInt] = # Replace with your value
worker_timeout: Optional[StrictInt] = None
ordering: Optional[StrictStr] = "example_ordering"
run_worker_action_response_instance = RunWorkerActionResponse(type=type, worker_id=worker_id, worker_as_at=worker_as_at, worker_parameters=worker_parameters, worker_status_triggers=worker_status_triggers, child_task_configurations=child_task_configurations, re_run_configurations=re_run_configurations, worker_timeout=worker_timeout, ordering=ordering)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

