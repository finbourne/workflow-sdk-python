# PagedResourceListOfEventHandler


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[EventHandler]**](EventHandler.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid_workflow.models.paged_resource_list_of_event_handler import PagedResourceListOfEventHandler

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfEventHandler from a JSON string
paged_resource_list_of_event_handler_instance = PagedResourceListOfEventHandler.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfEventHandler.to_json()

# convert the object into a dict
paged_resource_list_of_event_handler_dict = paged_resource_list_of_event_handler_instance.to_dict()
# create an instance of PagedResourceListOfEventHandler from a dict
paged_resource_list_of_event_handler_form_dict = paged_resource_list_of_event_handler.from_dict(paged_resource_list_of_event_handler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


