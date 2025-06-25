# TransitionTriggerDefinition

State changes happen in response to Triggers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The key/Name of this Trigger | 
**trigger** | [**TriggerSchema**](TriggerSchema.md) |  | 
**display_name** | **str** | Display name for trigger | [optional] 
**description** | **str** | Description of trigger | [optional] 

## Example

```python
from lusid_workflow.models.transition_trigger_definition import TransitionTriggerDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of TransitionTriggerDefinition from a JSON string
transition_trigger_definition_instance = TransitionTriggerDefinition.from_json(json)
# print the JSON string representation of the object
print TransitionTriggerDefinition.to_json()

# convert the object into a dict
transition_trigger_definition_dict = transition_trigger_definition_instance.to_dict()
# create an instance of TransitionTriggerDefinition from a dict
transition_trigger_definition_form_dict = transition_trigger_definition.from_dict(transition_trigger_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


