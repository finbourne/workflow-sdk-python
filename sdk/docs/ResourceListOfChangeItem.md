# ResourceListOfChangeItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ChangeItem]**](ChangeItem.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid_workflow.models.resource_list_of_change_item import ResourceListOfChangeItem

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfChangeItem from a JSON string
resource_list_of_change_item_instance = ResourceListOfChangeItem.from_json(json)
# print the JSON string representation of the object
print ResourceListOfChangeItem.to_json()

# convert the object into a dict
resource_list_of_change_item_dict = resource_list_of_change_item_instance.to_dict()
# create an instance of ResourceListOfChangeItem from a dict
resource_list_of_change_item_form_dict = resource_list_of_change_item.from_dict(resource_list_of_change_item_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


