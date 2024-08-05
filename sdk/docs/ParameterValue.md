# ParameterValue

Defines a Parameter Value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**value** | **object** | Value which can be a String, Boolean, Decimal or DateTime (ISO 8601) | [optional] 

## Example

```python
from lusid_workflow.models.parameter_value import ParameterValue

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterValue from a JSON string
parameter_value_instance = ParameterValue.from_json(json)
# print the JSON string representation of the object
print ParameterValue.to_json()

# convert the object into a dict
parameter_value_dict = parameter_value_instance.to_dict()
# create an instance of ParameterValue from a dict
parameter_value_form_dict = parameter_value.from_dict(parameter_value_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


