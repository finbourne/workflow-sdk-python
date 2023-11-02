# ResultField

Defines a Worker Result Field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**type** | **str** | The type of this Parameter | 
**display_name** | **str** | DisplayName | [optional] 
**description** | **str** | Description | [optional] 

## Example

```python
from lusid_workflow.models.result_field import ResultField

# TODO update the JSON string below
json = "{}"
# create an instance of ResultField from a JSON string
result_field_instance = ResultField.from_json(json)
# print the JSON string representation of the object
print ResultField.to_json()

# convert the object into a dict
result_field_dict = result_field_instance.to_dict()
# create an instance of ResultField from a dict
result_field_form_dict = result_field.from_dict(result_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


