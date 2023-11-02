# ActionDefinition

Defines the Actions for a Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of this Action | 
**action_details** | [**ActionDetails**](ActionDetails.md) |  | 

## Example

```python
from lusid_workflow.models.action_definition import ActionDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ActionDefinition from a JSON string
action_definition_instance = ActionDefinition.from_json(json)
# print the JSON string representation of the object
print ActionDefinition.to_json()

# convert the object into a dict
action_definition_dict = action_definition_instance.to_dict()
# create an instance of ActionDefinition from a dict
action_definition_form_dict = action_definition.from_dict(action_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


