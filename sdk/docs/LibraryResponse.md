# LibraryResponse

Readonly configuration for any Library Worker
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | [optional] 
## Example

```python
from lusid_workflow.models.library_response import LibraryResponse
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator

type: Optional[StrictStr] = "example_type"
library_response_instance = LibraryResponse(type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

