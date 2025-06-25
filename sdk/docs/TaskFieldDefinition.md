# TaskFieldDefinition

Defines a Task Definition Field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this Field | 
**type** | **str** | The value type for the field. Available values are: \&quot;String\&quot;, \&quot;Decimal\&quot;, \&quot;DateTime\&quot;, \&quot;Boolean\&quot;) | 
**read_only_states** | [**ReadOnlyStates**](ReadOnlyStates.md) |  | [optional] 
**value_constraints** | [**ValueConstraints**](ValueConstraints.md) |  | [optional] 
**display_name** | **str** | Display name for field definition | [optional] 
**description** | **str** | Description for field definition | [optional] 
**category** | **str** | Category for field definition | [optional] 
**contains_url** | **bool** | Field contains url | [optional] 

## Example

```python
from lusid_workflow.models.task_field_definition import TaskFieldDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of TaskFieldDefinition from a JSON string
task_field_definition_instance = TaskFieldDefinition.from_json(json)
# print the JSON string representation of the object
print TaskFieldDefinition.to_json()

# convert the object into a dict
task_field_definition_dict = task_field_definition_instance.to_dict()
# create an instance of TaskFieldDefinition from a dict
task_field_definition_form_dict = task_field_definition.from_dict(task_field_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


