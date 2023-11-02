# ActionDefinitionResponse

Defines the Actions for a Task in a read-only form

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of this Action | [optional] 
**action_details** | [**ActionDetailsResponse**](ActionDetailsResponse.md) |  | [optional] 

## Example

```python
from lusid_workflow.models.action_definition_response import ActionDefinitionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionDefinitionResponse from a JSON string
action_definition_response_instance = ActionDefinitionResponse.from_json(json)
# print the JSON string representation of the object
print ActionDefinitionResponse.to_json()

# convert the object into a dict
action_definition_response_dict = action_definition_response_instance.to_dict()
# create an instance of ActionDefinitionResponse from a dict
action_definition_response_form_dict = action_definition_response.from_dict(action_definition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


