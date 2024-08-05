# EventMatchingPattern

The matching event pattern object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The type of event to subscribe to. The list of available event types can be discovered  by calling the ‘List available EventTypes’ API endpoint in the Notifications service | 
**filter** | **str** | A filter on the event. See https://support.lusid.com/filtering-results-from-lusid for more information.  If not provided, all events will be matched. | [optional] 

## Example

```python
from lusid_workflow.models.event_matching_pattern import EventMatchingPattern

# TODO update the JSON string below
json = "{}"
# create an instance of EventMatchingPattern from a JSON string
event_matching_pattern_instance = EventMatchingPattern.from_json(json)
# print the JSON string representation of the object
print EventMatchingPattern.to_json()

# convert the object into a dict
event_matching_pattern_dict = event_matching_pattern_instance.to_dict()
# create an instance of EventMatchingPattern from a dict
event_matching_pattern_form_dict = event_matching_pattern.from_dict(event_matching_pattern_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


