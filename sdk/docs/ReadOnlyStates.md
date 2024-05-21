# ReadOnlyStates

Information about which states the field can be edited in

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_type** | **str** | The State Type (e.g. InitialState, AllStates, TerminalState, SelectedStates) | 
**selected_states** | **List[str]** | Named states for which the field will be readonly - This field can only be populated if StateType &#x3D; SelectedStates | [optional] 

## Example

```python
from lusid_workflow.models.read_only_states import ReadOnlyStates

# TODO update the JSON string below
json = "{}"
# create an instance of ReadOnlyStates from a JSON string
read_only_states_instance = ReadOnlyStates.from_json(json)
# print the JSON string representation of the object
print ReadOnlyStates.to_json()

# convert the object into a dict
read_only_states_dict = read_only_states_instance.to_dict()
# create an instance of ReadOnlyStates from a dict
read_only_states_form_dict = read_only_states.from_dict(read_only_states_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


