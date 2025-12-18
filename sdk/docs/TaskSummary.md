# TaskSummary

Summary of a Task created based on a Task Definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id for this Task | 
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**task_definition_version** | [**TaskDefinitionVersion**](TaskDefinitionVersion.md) |  | 
**task_definition_display_name** | **str** | The display name of the Task Definition used by this Task | 
**state** | **str** | Current State | 
## Example

```python
from lusid_workflow.models.task_summary import TaskSummary
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
task_definition_id: ResourceId = # Replace with your value
task_definition_version: TaskDefinitionVersion = # Replace with your value
task_definition_display_name: StrictStr = "example_task_definition_display_name"
state: StrictStr = "example_state"
task_summary_instance = TaskSummary(id=id, task_definition_id=task_definition_id, task_definition_version=task_definition_version, task_definition_display_name=task_definition_display_name, state=state)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

