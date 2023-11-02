# PagedResourceListOfWorker


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[Worker]**](Worker.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid_workflow.models.paged_resource_list_of_worker import PagedResourceListOfWorker

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfWorker from a JSON string
paged_resource_list_of_worker_instance = PagedResourceListOfWorker.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfWorker.to_json()

# convert the object into a dict
paged_resource_list_of_worker_dict = paged_resource_list_of_worker_instance.to_dict()
# create an instance of PagedResourceListOfWorker from a dict
paged_resource_list_of_worker_form_dict = paged_resource_list_of_worker.from_dict(paged_resource_list_of_worker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


