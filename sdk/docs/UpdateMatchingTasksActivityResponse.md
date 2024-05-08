# UpdateMatchingTasksActivityResponse

Readonly TaskActivity response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of task activity | [optional] 
**filter** | **str** | The filter that matches on existing tasks | [optional] 
**trigger** | **str** | Trigger to supply to all tasks that have been matched | [optional] 
**correlation_ids** | [**List[EventHandlerMapping]**](EventHandlerMapping.md) | The event to correlation ID mappings | [optional] 
**task_fields** | [**Dict[str, FieldMapping]**](FieldMapping.md) | The event to task field mappings | [optional] 

## Example

```python
from lusid_workflow.models.update_matching_tasks_activity_response import UpdateMatchingTasksActivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMatchingTasksActivityResponse from a JSON string
update_matching_tasks_activity_response_instance = UpdateMatchingTasksActivityResponse.from_json(json)
# print the JSON string representation of the object
print UpdateMatchingTasksActivityResponse.to_json()

# convert the object into a dict
update_matching_tasks_activity_response_dict = update_matching_tasks_activity_response_instance.to_dict()
# create an instance of UpdateMatchingTasksActivityResponse from a dict
update_matching_tasks_activity_response_form_dict = update_matching_tasks_activity_response.from_dict(update_matching_tasks_activity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


