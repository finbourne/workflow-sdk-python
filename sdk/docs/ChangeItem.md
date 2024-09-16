# ChangeItem

Defines a change that occured to a Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_modified** | **datetime** | The AsAt time of the change | 
**user_id_modified** | **str** | The User ID that performed the change | 
**request_id_modified** | **str** | The Request ID of the request that caused the change | 
**as_at_version_number** | **int** | The AsAt Version number | 
**action** | **str** | The Action that resulted in the change | 
**attribute_name** | **str** | The name of the attribute that has been change | 
**previous_value** | **object** | The value of the attribute prior to the change | [optional] 
**new_value** | **object** | The value of the attribute following the change | 

## Example

```python
from lusid_workflow.models.change_item import ChangeItem

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeItem from a JSON string
change_item_instance = ChangeItem.from_json(json)
# print the JSON string representation of the object
print ChangeItem.to_json()

# convert the object into a dict
change_item_dict = change_item_instance.to_dict()
# create an instance of ChangeItem from a dict
change_item_form_dict = change_item.from_dict(change_item_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


