# CreateChildTaskConfiguration

Create Child Task Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**task_definition_as_at** | **datetime** | TaskDefinition AsAt timestamp | [optional] 
**initial_trigger** | **str** | The Initial Trigger for automatic start | [optional] 
**child_task_fields** | [**Dict[str, FieldMapping]**](FieldMapping.md) | Field Mappings | [optional] 
**map_stacking_key_from** | **str** | If present, the value of this field on the parent task will be the Stacking Key on any created child tasks | [optional] 

## Example

```python
from lusid_workflow.models.create_child_task_configuration import CreateChildTaskConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChildTaskConfiguration from a JSON string
create_child_task_configuration_instance = CreateChildTaskConfiguration.from_json(json)
# print the JSON string representation of the object
print CreateChildTaskConfiguration.to_json()

# convert the object into a dict
create_child_task_configuration_dict = create_child_task_configuration_instance.to_dict()
# create an instance of CreateChildTaskConfiguration from a dict
create_child_task_configuration_form_dict = create_child_task_configuration.from_dict(create_child_task_configuration_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


