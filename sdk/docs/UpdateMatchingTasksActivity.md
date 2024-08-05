# UpdateMatchingTasksActivity

Update all matching tasks based on filter matches

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of task activity | 
**filter** | **str** | The filter that matches on existing tasks | [optional] 
**trigger** | **str** | Trigger to supply to all tasks that have been matched | 
**correlation_ids** | [**List[EventHandlerMapping]**](EventHandlerMapping.md) | The event to correlation ID mappings | [optional] 
**task_fields** | [**Dict[str, FieldMapping]**](FieldMapping.md) | The event to task field mappings | [optional] 

## Example

```python
from lusid_workflow.models.update_matching_tasks_activity import UpdateMatchingTasksActivity

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMatchingTasksActivity from a JSON string
update_matching_tasks_activity_instance = UpdateMatchingTasksActivity.from_json(json)
# print the JSON string representation of the object
print UpdateMatchingTasksActivity.to_json()

# convert the object into a dict
update_matching_tasks_activity_dict = update_matching_tasks_activity_instance.to_dict()
# create an instance of UpdateMatchingTasksActivity from a dict
update_matching_tasks_activity_form_dict = update_matching_tasks_activity.from_dict(update_matching_tasks_activity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


