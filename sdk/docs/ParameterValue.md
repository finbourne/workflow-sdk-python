# ParameterValue

Defines a Parameter Value
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**value** | **object** | Value which can be a String, Boolean, Decimal or DateTime (ISO 8601) | [optional] 
## Example

```python
from lusid_workflow.models.parameter_value import ParameterValue
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
value: Optional[Any] = # Replace with your value
parameter_value_instance = ParameterValue(name=name, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

