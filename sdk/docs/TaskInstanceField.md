# TaskInstanceField

Defines a Field on a Task
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this Field | 
**value** | **object** | The value of this Field | [optional] 
## Example

```python
from lusid_workflow.models.task_instance_field import TaskInstanceField
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

name: StrictStr = "example_name"
value: Optional[Any] = # Replace with your value
task_instance_field_instance = TaskInstanceField(name=name, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

