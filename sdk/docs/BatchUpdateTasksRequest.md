# BatchUpdateTasksRequest

A request to update multiple Tasks

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_tasks** | [**List[UpdateTaskWithIdAndTriggerRequest]**](UpdateTaskWithIdAndTriggerRequest.md) | A Dictionary of task IDs to UpdateTaskRequest | [optional] 

## Example

```python
from lusid_workflow.models.batch_update_tasks_request import BatchUpdateTasksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdateTasksRequest from a JSON string
batch_update_tasks_request_instance = BatchUpdateTasksRequest.from_json(json)
# print the JSON string representation of the object
print BatchUpdateTasksRequest.to_json()

# convert the object into a dict
batch_update_tasks_request_dict = batch_update_tasks_request_instance.to_dict()
# create an instance of BatchUpdateTasksRequest from a dict
batch_update_tasks_request_form_dict = batch_update_tasks_request.from_dict(batch_update_tasks_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


