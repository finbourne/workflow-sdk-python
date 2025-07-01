# LuminesceView

Configuration for a Worker that calls a Luminesce view
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | 
**name** | **str** | Name of the view in Luminesce | 
## Example

```python
from lusid_workflow.models.luminesce_view import LuminesceView
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

type: StrictStr = "example_type"
name: StrictStr = "example_name"
luminesce_view_instance = LuminesceView(type=type, name=name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

