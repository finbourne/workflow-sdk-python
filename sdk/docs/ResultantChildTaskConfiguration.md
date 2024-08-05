# ResultantChildTaskConfiguration

Child Task Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_matching_pattern** | [**ResultMatchingPattern**](ResultMatchingPattern.md) |  | [optional] 
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**task_definition_as_at** | **datetime** | TaskDefinition AsAt timestamp | [optional] 
**initial_trigger** | **str** | The Initial Trigger for automatic start | [optional] 
**child_task_fields** | [**Dict[str, FieldMapping]**](FieldMapping.md) | Field Mappings | 
**map_stacking_key_from** | **str** | The field to be mapped as the ChildTasks Stacking Key | [optional] 

## Example

```python
from lusid_workflow.models.resultant_child_task_configuration import ResultantChildTaskConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ResultantChildTaskConfiguration from a JSON string
resultant_child_task_configuration_instance = ResultantChildTaskConfiguration.from_json(json)
# print the JSON string representation of the object
print ResultantChildTaskConfiguration.to_json()

# convert the object into a dict
resultant_child_task_configuration_dict = resultant_child_task_configuration_instance.to_dict()
# create an instance of ResultantChildTaskConfiguration from a dict
resultant_child_task_configuration_form_dict = resultant_child_task_configuration.from_dict(resultant_child_task_configuration_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


