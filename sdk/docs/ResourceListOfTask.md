# ResourceListOfTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Task]**](Task.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid_workflow.models.resource_list_of_task import ResourceListOfTask

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfTask from a JSON string
resource_list_of_task_instance = ResourceListOfTask.from_json(json)
# print the JSON string representation of the object
print ResourceListOfTask.to_json()

# convert the object into a dict
resource_list_of_task_dict = resource_list_of_task_instance.to_dict()
# create an instance of ResourceListOfTask from a dict
resource_list_of_task_form_dict = resource_list_of_task.from_dict(resource_list_of_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


