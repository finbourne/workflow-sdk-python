# ResultField

Defines a Worker Result Field
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**type** | **str** | The type of this Parameter | 
**display_name** | **str** | DisplayName | [optional] 
**description** | **str** | Description | [optional] 
## Example

```python
from lusid_workflow.models.result_field import ResultField
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
type: StrictStr = "example_type"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
result_field_instance = ResultField(name=name, type=type, display_name=display_name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

