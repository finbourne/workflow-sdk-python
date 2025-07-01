# LuminesceViewResponse

Readonly configuration for a Worker that calls a Luminesce view
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | [optional] 
**name** | **str** | Name of the view in Luminesce | [optional] 
## Example

```python
from lusid_workflow.models.luminesce_view_response import LuminesceViewResponse
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator

type: Optional[StrictStr] = "example_type"
name: Optional[StrictStr] = "example_name"
luminesce_view_response_instance = LuminesceViewResponse(type=type, name=name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

