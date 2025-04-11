# BatchUpdateTasksResponse

Defines a representation of tasks that have been updated

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Task]**](Task.md) | Successful tasks brought back from the BatchUpdate call | [optional] [readonly] 
**failed** | [**List[ErrorDetail]**](ErrorDetail.md) | Individual failures for each task returned from the BatchUpdate call | [optional] [readonly] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid_workflow.models.batch_update_tasks_response import BatchUpdateTasksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdateTasksResponse from a JSON string
batch_update_tasks_response_instance = BatchUpdateTasksResponse.from_json(json)
# print the JSON string representation of the object
print BatchUpdateTasksResponse.to_json()

# convert the object into a dict
batch_update_tasks_response_dict = batch_update_tasks_response_instance.to_dict()
# create an instance of BatchUpdateTasksResponse from a dict
batch_update_tasks_response_form_dict = batch_update_tasks_response.from_dict(batch_update_tasks_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


