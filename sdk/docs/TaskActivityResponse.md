# TaskActivityResponse

Readonly information about how the worker should be executed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of task activity | [optional] 
**correlation_ids** | [**List[EventHandlerMapping]**](EventHandlerMapping.md) | The event to correlation ID mappings | [optional] 
**task_fields** | [**Dict[str, FieldMapping]**](FieldMapping.md) | The event to task field mappings | [optional] 
**initial_trigger** | **str** | Trigger to supply to all tasks to be made | [optional] 
**filter** | **str** | The filter that matches on existing tasks | [optional] 
**trigger** | **str** | Trigger to supply to all tasks that have been matched | [optional] 

## Example

```python
from lusid_workflow.models.task_activity_response import TaskActivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskActivityResponse from a JSON string
task_activity_response_instance = TaskActivityResponse.from_json(json)
# print the JSON string representation of the object
print TaskActivityResponse.to_json()

# convert the object into a dict
task_activity_response_dict = task_activity_response_instance.to_dict()
# create an instance of TaskActivityResponse from a dict
task_activity_response_form_dict = task_activity_response.from_dict(task_activity_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


