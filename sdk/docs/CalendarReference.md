# CalendarReference

Reference to a Calendar in LUSID
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the Calendar | 
**code** | **str** | The code of the Calendar | 
## Example

```python
from lusid_workflow.models.calendar_reference import CalendarReference
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
calendar_reference_instance = CalendarReference(scope=scope, code=code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

