# CutLabelReference

A reference to a Cut Label in LUSID
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of the Cut Label | 
**type** | **str** | The type of Time of Day | 
## Example

```python
from lusid_workflow.models.cut_label_reference import CutLabelReference
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

code: StrictStr = "example_code"
type: StrictStr = "example_type"
cut_label_reference_instance = CutLabelReference(code=code, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

