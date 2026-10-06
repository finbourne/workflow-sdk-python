# WorkflowRun

Information about the run of the Workflow that created this Task, inherited from the root/ultimate parent Task.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of this run of the Workflow. Assigned once, when the run is instantiated. | 
**as_at_created** | **datetime** | The version.asAtCreated of the root/ultimate parent Task of this run. | 
**completion_status** | **str** | The completion status of the root/ultimate parent Task of this run: NotStarted, InProgress, or Completed. | 
## Example

```python
from lusid_workflow.models.workflow_run import WorkflowRun
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictInt = # Replace with your value
id: StrictInt = 42
as_at_created: datetime = # Replace with your value
completion_status: StrictStr = "example_completion_status"
workflow_run_instance = WorkflowRun(id=id, as_at_created=as_at_created, completion_status=completion_status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

