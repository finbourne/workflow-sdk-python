# CreateNewTaskActivity

Define a Task Activity that creates a new task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_trigger** | **str** | Trigger to supply to all tasks to be made | [optional] 
**type** | **str** | The type of task activity | 
**correlation_ids** | [**List[EventHandlerMapping]**](EventHandlerMapping.md) | The event to correlation ID mappings | [optional] 
**task_fields** | [**Dict[str, FieldMapping]**](FieldMapping.md) | The event to task field mappings | [optional] 

## Example

```python
from lusid_workflow.models.create_new_task_activity import CreateNewTaskActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewTaskActivity from a JSON string
create_new_task_activity_instance = CreateNewTaskActivity.from_json(json)
# print the JSON string representation of the object
print CreateNewTaskActivity.to_json()

# convert the object into a dict
create_new_task_activity_dict = create_new_task_activity_instance.to_dict()
# create an instance of CreateNewTaskActivity from a dict
create_new_task_activity_form_dict = create_new_task_activity.from_dict(create_new_task_activity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


