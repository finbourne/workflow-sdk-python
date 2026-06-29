# PerpetualProperty

A perpetual property (i.e. without effective dates) on a Workflow. A property is deleted by supplying a null Finbourne.Workflow.WebApi.Common.Dto.Json.Properties.PerpetualProperty.Value.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The property key in the form {domain}/{scope}/{code}. The domain must be &#39;Workflow&#39;. | 
**value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
## Example

```python
from lusid_workflow.models.perpetual_property import PerpetualProperty
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
value: Optional[PropertyValue] = None
perpetual_property_instance = PerpetualProperty(key=key, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

