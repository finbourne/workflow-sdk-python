# EventHandler

Information about an Event Handler

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**version** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**status** | **str** | The current status of the event handler | 
**event_matching_pattern** | [**EventMatchingPattern**](EventMatchingPattern.md) |  | 
**run_as_user_id** | [**EventHandlerMapping**](EventHandlerMapping.md) |  | 
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**task_definition_as_at** | **datetime** | AsAt of the required task definition | [optional] 
**task_activity** | [**TaskActivityResponse**](TaskActivityResponse.md) |  | 

## Example

```python
from lusid_workflow.models.event_handler import EventHandler

# TODO update the JSON string below
json = "{}"
# create an instance of EventHandler from a JSON string
event_handler_instance = EventHandler.from_json(json)
# print the JSON string representation of the object
print EventHandler.to_json()

# convert the object into a dict
event_handler_dict = event_handler_instance.to_dict()
# create an instance of EventHandler from a dict
event_handler_form_dict = event_handler.from_dict(event_handler_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


