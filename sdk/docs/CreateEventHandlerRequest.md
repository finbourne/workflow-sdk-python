# CreateEventHandlerRequest

Contains information for creating an Event Handler

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
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
from lusid_workflow.models.create_event_handler_request import CreateEventHandlerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventHandlerRequest from a JSON string
create_event_handler_request_instance = CreateEventHandlerRequest.from_json(json)
# print the JSON string representation of the object
print CreateEventHandlerRequest.to_json()

# convert the object into a dict
create_event_handler_request_dict = create_event_handler_request_instance.to_dict()
# create an instance of CreateEventHandlerRequest from a dict
create_event_handler_request_form_dict = create_event_handler_request.from_dict(create_event_handler_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


