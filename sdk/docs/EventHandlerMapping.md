# EventHandlerMapping

Defines a mapping for event handler properties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map_from** | **str** | The field to map from | [optional] 
**set_to** | **str** | The (constant) value to set | [optional] 

## Example

```python
from lusid_workflow.models.event_handler_mapping import EventHandlerMapping

# TODO update the JSON string below
json = "{}"
# create an instance of EventHandlerMapping from a JSON string
event_handler_mapping_instance = EventHandlerMapping.from_json(json)
# print the JSON string representation of the object
print EventHandlerMapping.to_json()

# convert the object into a dict
event_handler_mapping_dict = event_handler_mapping_instance.to_dict()
# create an instance of EventHandlerMapping from a dict
event_handler_mapping_form_dict = event_handler_mapping.from_dict(event_handler_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


