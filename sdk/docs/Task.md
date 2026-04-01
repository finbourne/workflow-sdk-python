# Task

Defines a Task created based on a Task Definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id for this Task | 
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**task_definition_version** | [**TaskDefinitionVersion**](TaskDefinitionVersion.md) |  | 
**task_definition_display_name** | **str** | The display name of the Task Definition used by this Task | 
**workflow_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**workflow_display_name** | **str** | The display name of the Workflow that this Task is a member of, if any | [optional] 
**state** | **str** | Current State | 
**ultimate_parent_task** | [**TaskSummary**](TaskSummary.md) |  | 
**parent_task** | [**TaskSummary**](TaskSummary.md) |  | [optional] 
**child_tasks** | [**List[TaskSummary]**](TaskSummary.md) | This Task&#39;s child tasks | [optional] 
**correlation_ids** | **List[str]** | User-provided ID used to link entities and tasks | [optional] 
**version** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
**terminal_state** | **bool** | True if no onward transitions are possible | 
**as_at_last_transition** | **datetime** | Last Transition timestamp | [optional] 
**fields** | [**List[TaskInstanceField]**](TaskInstanceField.md) | Fields and their latest values - should correspond with the Task Definition field schema | [optional] 
**stacking_key** | **str** | The key used to determine which stack to add the Task to | [optional] 
**stack** | [**Stack**](Stack.md) |  | [optional] 
**action_log_id_created** | **str** | The Id of the Action that created this Task | [optional] 
**action_log_id_modified** | **str** | The Id of the Action that last modified this Task | [optional] 
**action_log_id_submitted** | **str** | The Id of the last Action submitted by this Task | [optional] 
**hierarchical_position** | **str** | The hierarchical position of this Task: UltimateParent, IntermediateParent, Child, or Standalone | [optional] 
**completion_status** | **str** | The completion status of this Task: NotStarted, InProgress, or Completed | [optional] 
**open_duration** | **int** | Duration in seconds since the Task was created. If the Task is Completed, this is the duration from creation to the last transition. | [optional] 
**open_duration_since_last_update** | **int** | Duration in seconds since the Task was last updated. 0 if the Task is Completed. | [optional] 
**open_duration_since_last_transition** | **int** | Duration in seconds since the Task last transitioned. 0 if the Task is Completed. | [optional] 
## Example

```python
from lusid_workflow.models.task import Task
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
task_definition_id: ResourceId = # Replace with your value
task_definition_version: TaskDefinitionVersion = # Replace with your value
task_definition_display_name: StrictStr = "example_task_definition_display_name"
workflow_id: Optional[ResourceId] = # Replace with your value
workflow_display_name: Optional[StrictStr] = "example_workflow_display_name"
state: StrictStr = "example_state"
ultimate_parent_task: TaskSummary = # Replace with your value
parent_task: Optional[TaskSummary] = # Replace with your value
child_tasks: Optional[List[TaskSummary]] = # Replace with your value
correlation_ids: Optional[List[StrictStr]] = # Replace with your value
version: Optional[VersionInfo] = None
terminal_state: StrictBool = # Replace with your value
terminal_state:StrictBool = True
as_at_last_transition: Optional[datetime] = # Replace with your value
fields: Optional[List[TaskInstanceField]] = # Replace with your value
stacking_key: Optional[StrictStr] = "example_stacking_key"
stack: Optional[Stack] = None
action_log_id_created: Optional[StrictStr] = "example_action_log_id_created"
action_log_id_modified: Optional[StrictStr] = "example_action_log_id_modified"
action_log_id_submitted: Optional[StrictStr] = "example_action_log_id_submitted"
hierarchical_position: Optional[StrictStr] = "example_hierarchical_position"
completion_status: Optional[StrictStr] = "example_completion_status"
open_duration: Optional[StrictInt] = # Replace with your value
open_duration_since_last_update: Optional[StrictInt] = # Replace with your value
open_duration_since_last_transition: Optional[StrictInt] = # Replace with your value
task_instance = Task(id=id, task_definition_id=task_definition_id, task_definition_version=task_definition_version, task_definition_display_name=task_definition_display_name, workflow_id=workflow_id, workflow_display_name=workflow_display_name, state=state, ultimate_parent_task=ultimate_parent_task, parent_task=parent_task, child_tasks=child_tasks, correlation_ids=correlation_ids, version=version, terminal_state=terminal_state, as_at_last_transition=as_at_last_transition, fields=fields, stacking_key=stacking_key, stack=stack, action_log_id_created=action_log_id_created, action_log_id_modified=action_log_id_modified, action_log_id_submitted=action_log_id_submitted, hierarchical_position=hierarchical_position, completion_status=completion_status, open_duration=open_duration, open_duration_since_last_update=open_duration_since_last_update, open_duration_since_last_transition=open_duration_since_last_transition)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

