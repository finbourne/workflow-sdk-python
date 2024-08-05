# TaskActivity

Information about what tasks to create/update when receiving events

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of task activity | 
**correlation_ids** | [**List[EventHandlerMapping]**](EventHandlerMapping.md) | The event to correlation ID mappings | [optional] 
**task_fields** | [**Dict[str, FieldMapping]**](FieldMapping.md) | The event to task field mappings | [optional] 
**initial_trigger** | **str** | Trigger to supply to all tasks to be made | [optional] 
**filter** | **str** | The filter that matches on existing tasks | [optional] 
**trigger** | **str** | Trigger to supply to all tasks that have been matched | 

## Example

```python
from lusid_workflow.models.task_activity import TaskActivity

# TODO update the JSON string below
json = "{}"
# create an instance of TaskActivity from a JSON string
task_activity_instance = TaskActivity.from_json(json)
# print the JSON string representation of the object
print TaskActivity.to_json()

# convert the object into a dict
task_activity_dict = task_activity_instance.to_dict()
# create an instance of TaskActivity from a dict
task_activity_form_dict = task_activity.from_dict(task_activity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


