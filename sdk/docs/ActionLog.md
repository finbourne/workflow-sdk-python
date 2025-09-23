# ActionLog

An Action Log contains the processing history of an Action
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the Action | 
**origin** | [**ActionLogOrigin**](ActionLogOrigin.md) |  | 
**action_type** | **str** | The type of the Action | 
**run_as_user_id** | **str** | The ID of the user that the Action was performed by. If not specified, the actions were performed by the \&quot;current user\&quot;. | [optional] 
**logged_items** | [**List[ActionLogItem]**](ActionLogItem.md) | The logged items for this Action | 
## Example

```python
from lusid_workflow.models.action_log import ActionLog
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

id: StrictStr = "example_id"
origin: ActionLogOrigin = # Replace with your value
action_type: StrictStr = "example_action_type"
run_as_user_id: Optional[StrictStr] = "example_run_as_user_id"
logged_items: conlist(ActionLogItem) = # Replace with your value
action_log_instance = ActionLog(id=id, origin=origin, action_type=action_type, run_as_user_id=run_as_user_id, logged_items=logged_items)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

