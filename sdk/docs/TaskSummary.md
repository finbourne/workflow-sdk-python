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

# TODO update the JSON string below
json = "{}"
# create an instance of TaskSummary from a JSON string
task_summary_instance = TaskSummary.from_json(json)
# print the JSON string representation of the object
print TaskSummary.to_json()

# convert the object into a dict
task_summary_dict = task_summary_instance.to_dict()
# create an instance of TaskSummary from a dict
task_summary_form_dict = task_summary.from_dict(task_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


