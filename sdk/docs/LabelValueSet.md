# LabelValueSet

The set of string labels that make up a multi-value property.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** | The distinct string values of the multi-value property. | 
## Example

```python
from lusid_workflow.models.label_value_set import LabelValueSet
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: List[StrictStr] = # Replace with your value
label_value_set_instance = LabelValueSet(values=values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

