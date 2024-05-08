# UpdateEventHandlerRequest

Contains information for updating an Event Handler

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**status** | **str** | The current status of the event handler | 
**event_matching_pattern** | [**EventMatchingPattern**](EventMatchingPattern.md) |  | 
**run_as_user_id** | [**EventHandlerMapping**](EventHandlerMapping.md) |  | 
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**task_definition_as_at** | **datetime** | AsAt of the required task definition | [optional] 
**task_activity** | [**TaskActivity**](TaskActivity.md) |  | 

## Example

```python
from lusid_workflow.models.update_event_handler_request import UpdateEventHandlerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEventHandlerRequest from a JSON string
update_event_handler_request_instance = UpdateEventHandlerRequest.from_json(json)
# print the JSON string representation of the object
print UpdateEventHandlerRequest.to_json()

# convert the object into a dict
update_event_handler_request_dict = update_event_handler_request_instance.to_dict()
# create an instance of UpdateEventHandlerRequest from a dict
update_event_handler_request_form_dict = update_event_handler_request.from_dict(update_event_handler_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


