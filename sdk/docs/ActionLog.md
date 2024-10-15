# ActionLog

An Action Log contains the processing history of an Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the Action | 
**origin** | [**ActionLogOrigin**](ActionLogOrigin.md) |  | 
**action_type** | **str** | The type of the Action | 
**run_as_user_id** | **str** | The ID of the user that the Action was performed by.  If not specified, the actions were performed by the \&quot;current user\&quot;. | [optional] 
**logged_items** | [**List[ActionLogItem]**](ActionLogItem.md) | The logged items for this Action | 

## Example

```python
from lusid_workflow.models.action_log import ActionLog

# TODO update the JSON string below
json = "{}"
# create an instance of ActionLog from a JSON string
action_log_instance = ActionLog.from_json(json)
# print the JSON string representation of the object
print ActionLog.to_json()

# convert the object into a dict
action_log_dict = action_log_instance.to_dict()
# create an instance of ActionLog from a dict
action_log_form_dict = action_log.from_dict(action_log_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


