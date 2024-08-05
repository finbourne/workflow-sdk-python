# CreateNewTaskActivityResponse

Read only Create new task response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of task activity | [optional] 
**initial_trigger** | **str** | Trigger to supply to all tasks to be made | [optional] 
**correlation_ids** | [**List[EventHandlerMapping]**](EventHandlerMapping.md) | The event to correlation ID mappings | [optional] 
**task_fields** | [**Dict[str, FieldMapping]**](FieldMapping.md) | The event to task field mappings | [optional] 

## Example

```python
from lusid_workflow.models.create_new_task_activity_response import CreateNewTaskActivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewTaskActivityResponse from a JSON string
create_new_task_activity_response_instance = CreateNewTaskActivityResponse.from_json(json)
# print the JSON string representation of the object
print CreateNewTaskActivityResponse.to_json()

# convert the object into a dict
create_new_task_activity_response_dict = create_new_task_activity_response_instance.to_dict()
# create an instance of CreateNewTaskActivityResponse from a dict
create_new_task_activity_response_form_dict = create_new_task_activity_response.from_dict(create_new_task_activity_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


