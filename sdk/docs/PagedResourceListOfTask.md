# PagedResourceListOfTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[Task]**](Task.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid_workflow.models.paged_resource_list_of_task import PagedResourceListOfTask

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfTask from a JSON string
paged_resource_list_of_task_instance = PagedResourceListOfTask.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfTask.to_json()

# convert the object into a dict
paged_resource_list_of_task_dict = paged_resource_list_of_task_instance.to_dict()
# create an instance of PagedResourceListOfTask from a dict
paged_resource_list_of_task_form_dict = paged_resource_list_of_task.from_dict(paged_resource_list_of_task_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


