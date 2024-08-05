# FieldMapping

Defines a single Field map

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map_from** | **str** | The field to map from | [optional] 
**set_to** | **object** | The (constant) value to set | [optional] 

## Example

```python
from lusid_workflow.models.field_mapping import FieldMapping

# TODO update the JSON string below
json = "{}"
# create an instance of FieldMapping from a JSON string
field_mapping_instance = FieldMapping.from_json(json)
# print the JSON string representation of the object
print FieldMapping.to_json()

# convert the object into a dict
field_mapping_dict = field_mapping_instance.to_dict()
# create an instance of FieldMapping from a dict
field_mapping_form_dict = field_mapping.from_dict(field_mapping_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


