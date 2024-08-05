# InitialState

Defines the Initial State of the Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Initial State of the Task | 
**required_fields** | **List[str]** | Required input Fields for the Initial State | [optional] 

## Example

```python
from lusid_workflow.models.initial_state import InitialState

# TODO update the JSON string below
json = "{}"
# create an instance of InitialState from a JSON string
initial_state_instance = InitialState.from_json(json)
# print the JSON string representation of the object
print InitialState.to_json()

# convert the object into a dict
initial_state_dict = initial_state_instance.to_dict()
# create an instance of InitialState from a dict
initial_state_form_dict = initial_state.from_dict(initial_state_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


