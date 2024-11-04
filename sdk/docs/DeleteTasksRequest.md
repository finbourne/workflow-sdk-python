# DeleteTasksRequest

Contains required info to delete Tasks

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_ids** | **List[str]** | The Ids of the Tasks to delete | [optional] 

## Example

```python
from lusid_workflow.models.delete_tasks_request import DeleteTasksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTasksRequest from a JSON string
delete_tasks_request_instance = DeleteTasksRequest.from_json(json)
# print the JSON string representation of the object
print DeleteTasksRequest.to_json()

# convert the object into a dict
delete_tasks_request_dict = delete_tasks_request_instance.to_dict()
# create an instance of DeleteTasksRequest from a dict
delete_tasks_request_form_dict = delete_tasks_request.from_dict(delete_tasks_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


