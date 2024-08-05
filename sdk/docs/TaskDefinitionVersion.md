# TaskDefinitionVersion

The version of the Task Definition used by this Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_modified** | **datetime** | The asAt datetime of the Task Definition used by this Task | [optional] 

## Example

```python
from lusid_workflow.models.task_definition_version import TaskDefinitionVersion

# TODO update the JSON string below
json = "{}"
# create an instance of TaskDefinitionVersion from a JSON string
task_definition_version_instance = TaskDefinitionVersion.from_json(json)
# print the JSON string representation of the object
print TaskDefinitionVersion.to_json()

# convert the object into a dict
task_definition_version_dict = task_definition_version_instance.to_dict()
# create an instance of TaskDefinitionVersion from a dict
task_definition_version_form_dict = task_definition_version.from_dict(task_definition_version_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


