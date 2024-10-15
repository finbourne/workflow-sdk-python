# ActionLogOrigin

The Action Log Origin contains information about how the Action was created

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | The Id of the Task that created this Action | [optional] 
**request_id** | **str** | The request Id of the request that caused this Action to be triggered.  This could be the original request that caused a sequence of Actions that resulted in this Action | 

## Example

```python
from lusid_workflow.models.action_log_origin import ActionLogOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of ActionLogOrigin from a JSON string
action_log_origin_instance = ActionLogOrigin.from_json(json)
# print the JSON string representation of the object
print ActionLogOrigin.to_json()

# convert the object into a dict
action_log_origin_dict = action_log_origin_instance.to_dict()
# create an instance of ActionLogOrigin from a dict
action_log_origin_form_dict = action_log_origin.from_dict(action_log_origin_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


