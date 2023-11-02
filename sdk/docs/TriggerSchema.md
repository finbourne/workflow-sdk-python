# TriggerSchema

Triggers can operate in response to different stimuli

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of Trigger; available value(s): External | 

## Example

```python
from lusid_workflow.models.trigger_schema import TriggerSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerSchema from a JSON string
trigger_schema_instance = TriggerSchema.from_json(json)
# print the JSON string representation of the object
print TriggerSchema.to_json()

# convert the object into a dict
trigger_schema_dict = trigger_schema_instance.to_dict()
# create an instance of TriggerSchema from a dict
trigger_schema_form_dict = trigger_schema.from_dict(trigger_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


