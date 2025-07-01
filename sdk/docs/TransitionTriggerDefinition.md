# TransitionTriggerDefinition

State changes happen in response to Triggers
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The key/Name of this Trigger | 
**trigger** | [**TriggerSchema**](TriggerSchema.md) |  | 
**display_name** | **str** | Display name for trigger | [optional] 
**description** | **str** | Description of trigger | [optional] 
## Example

```python
from lusid_workflow.models.transition_trigger_definition import TransitionTriggerDefinition
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

name: StrictStr = "example_name"
trigger: TriggerSchema = # Replace with your value
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
transition_trigger_definition_instance = TransitionTriggerDefinition(name=name, trigger=trigger, display_name=display_name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

