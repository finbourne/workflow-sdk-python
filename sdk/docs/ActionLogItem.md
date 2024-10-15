# ActionLogItem

A log item for a given Action Log

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The timestamp of the log item | 
**log_type** | **str** | The type of log item | 
**details** | **str** | The details of the log item | [optional] 

## Example

```python
from lusid_workflow.models.action_log_item import ActionLogItem

# TODO update the JSON string below
json = "{}"
# create an instance of ActionLogItem from a JSON string
action_log_item_instance = ActionLogItem.from_json(json)
# print the JSON string representation of the object
print ActionLogItem.to_json()

# convert the object into a dict
action_log_item_dict = action_log_item_instance.to_dict()
# create an instance of ActionLogItem from a dict
action_log_item_form_dict = action_log_item.from_dict(action_log_item_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


