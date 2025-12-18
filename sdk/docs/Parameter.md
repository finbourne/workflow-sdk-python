# Parameter

Defines a Worker Parameter
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this Parameter | 
**name** | **str** | Name | 
**display_name** | **str** | DisplayName | [optional] 
**description** | **str** | Description | [optional] 
**required** | **bool** | Required or not | 
**default_value** | **str** | DefaultValue | [optional] 
## Example

```python
from lusid_workflow.models.parameter import Parameter
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
name: StrictStr = "example_name"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
required: StrictBool = # Replace with your value
required:StrictBool = True
default_value: Optional[StrictStr] = "example_default_value"
parameter_instance = Parameter(type=type, name=name, display_name=display_name, description=description, required=required, default_value=default_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

