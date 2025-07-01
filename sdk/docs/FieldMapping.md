# FieldMapping

Defines a single Field map
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map_from** | **str** | The field to map from | [optional] 
**set_to** | **object** | The (constant) value to set | [optional] 
## Example

```python
from lusid_workflow.models.field_mapping import FieldMapping
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

map_from: Optional[StrictStr] = "example_map_from"
set_to: Optional[Any] = # Replace with your value
field_mapping_instance = FieldMapping(map_from=map_from, set_to=set_to)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

