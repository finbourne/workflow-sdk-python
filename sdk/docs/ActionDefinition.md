# ActionDefinition

Defines the Actions for a Task
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of this Action | 
**run_as_user_id** | **str** | The ID of the user that this action will be performed by. If not specified, the actions will be performed by the \&quot;current user\&quot;. | [optional] 
**action_details** | [**ActionDetails**](ActionDetails.md) |  | 
**display_name** | **str** | The display name of this Action | [optional] 
**description** | **str** | The description of this Action | [optional] 
## Example

```python
from lusid_workflow.models.action_definition import ActionDefinition
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

name: StrictStr = "example_name"
run_as_user_id: Optional[StrictStr] = "example_run_as_user_id"
action_details: ActionDetails = # Replace with your value
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
action_definition_instance = ActionDefinition(name=name, run_as_user_id=run_as_user_id, action_details=action_details, display_name=display_name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

