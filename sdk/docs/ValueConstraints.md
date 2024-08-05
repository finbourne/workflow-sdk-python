# ValueConstraints

Constraints that should be applied to a Tasks fields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraint_type** | **str** | Whether the constraint is a suggestion or should be enforced via validation (e.g. Suggested, Validated) | 
**value_source_type** | **str** | The source of the acceptable values (e.g. AcceptableValues) | 
**acceptable_values** | **List[object]** | The acceptable values for the field | 

## Example

```python
from lusid_workflow.models.value_constraints import ValueConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of ValueConstraints from a JSON string
value_constraints_instance = ValueConstraints.from_json(json)
# print the JSON string representation of the object
print ValueConstraints.to_json()

# convert the object into a dict
value_constraints_dict = value_constraints_instance.to_dict()
# create an instance of ValueConstraints from a dict
value_constraints_form_dict = value_constraints.from_dict(value_constraints_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


