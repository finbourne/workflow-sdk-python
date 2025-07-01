# TaskStateDefinition

A Task Definition/Task has a given set of States
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of this State | 
**display_name** | **str** | The display name of this State | [optional] 
**description** | **str** | The description of this State | [optional] 
**category** | **str** | The category of this State | [optional] 
## Example

```python
from lusid_workflow.models.task_state_definition import TaskStateDefinition
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

name: StrictStr = "example_name"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
category: Optional[StrictStr] = "example_category"
task_state_definition_instance = TaskStateDefinition(name=name, display_name=display_name, description=description, category=category)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

