# TaskFieldDefinition

Defines a Task Definition Field
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this Field | 
**type** | **str** | The value type for the field. Available values are: \&quot;String\&quot;, \&quot;Decimal\&quot;, \&quot;DateTime\&quot;, \&quot;Boolean\&quot;) | 
**read_only_states** | [**ReadOnlyStates**](ReadOnlyStates.md) |  | [optional] 
**value_constraints** | [**ValueConstraints**](ValueConstraints.md) |  | [optional] 
**display_name** | **str** | Display name for field definition | [optional] 
**description** | **str** | Description for field definition | [optional] 
**category** | **str** | Category for field definition | [optional] 
**contains_url** | **bool** | Field contains url | [optional] 
## Example

```python
from lusid_workflow.models.task_field_definition import TaskFieldDefinition
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, constr, validator

name: StrictStr = "example_name"
type: StrictStr = "example_type"
read_only_states: Optional[ReadOnlyStates] = # Replace with your value
value_constraints: Optional[ValueConstraints] = # Replace with your value
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
category: Optional[StrictStr] = "example_category"
contains_url: Optional[StrictBool] = # Replace with your value
contains_url:Optional[StrictBool] = None
task_field_definition_instance = TaskFieldDefinition(name=name, type=type, read_only_states=read_only_states, value_constraints=value_constraints, display_name=display_name, description=description, category=category, contains_url=contains_url)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

