# TaskInstanceField

Defines a Field on a Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this Field | 
**value** | **object** | The value of this Field | [optional] 

## Example

```python
from lusid_workflow.models.task_instance_field import TaskInstanceField

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInstanceField from a JSON string
task_instance_field_instance = TaskInstanceField.from_json(json)
# print the JSON string representation of the object
print TaskInstanceField.to_json()

# convert the object into a dict
task_instance_field_dict = task_instance_field_instance.to_dict()
# create an instance of TaskInstanceField from a dict
task_instance_field_form_dict = task_instance_field.from_dict(task_instance_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


