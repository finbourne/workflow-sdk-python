# ActionDefinitionResponse

Defines the Actions for a Task in a read-only form
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of this Action | [optional] 
**run_as_user_id** | **str** | The ID of the user that this action will be performed by. If not specified, the actions will be performed by the \&quot;current user\&quot;. | [optional] 
**action_details** | [**ActionDetailsResponse**](ActionDetailsResponse.md) |  | [optional] 
**display_name** | **str** | Schema for the Action | [optional] 
**description** | **str** | Schema for the Action | [optional] 
**category** | **str** | Schema for the Action | [optional] 
## Example

```python
from lusid_workflow.models.action_definition_response import ActionDefinitionResponse
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

name: Optional[StrictStr] = "example_name"
run_as_user_id: Optional[StrictStr] = "example_run_as_user_id"
action_details: Optional[ActionDetailsResponse] = # Replace with your value
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
category: Optional[StrictStr] = "example_category"
action_definition_response_instance = ActionDefinitionResponse(name=name, run_as_user_id=run_as_user_id, action_details=action_details, display_name=display_name, description=description, category=category)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

