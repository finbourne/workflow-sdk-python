# Parameter

Defines a Worker Parameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this Parameter | 
**name** | **str** | Name | 
**display_name** | **str** | DisplayName | [optional] 
**description** | **str** | Description | [optional] 
**required** | **bool** | Required or not | 
**default_value** | **str** | DefaultValue | [optional] 

## Example

```python
from lusid_workflow.models.parameter import Parameter

# TODO update the JSON string below
json = "{}"
# create an instance of Parameter from a JSON string
parameter_instance = Parameter.from_json(json)
# print the JSON string representation of the object
print Parameter.to_json()

# convert the object into a dict
parameter_dict = parameter_instance.to_dict()
# create an instance of Parameter from a dict
parameter_form_dict = parameter.from_dict(parameter_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


