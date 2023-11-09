# Task

Defines a Task created based on a Task Definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id for this Task | 
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**task_definition_version** | [**TaskDefinitionVersion**](TaskDefinitionVersion.md) |  | 
**task_definition_display_name** | **str** | The display name of the Task Definition used by this Task | 
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

## Example

```python
from lusid_workflow.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print Task.to_json()

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_form_dict = task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


