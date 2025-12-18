# DeletedEntityResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The Uri related to this Entity | [optional] 
**effective_from** | **datetime** | The EffectiveFrom for this response | [optional] 
**as_at** | **datetime** | The AsAt for this response | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid_workflow.models.deleted_entity_response import DeletedEntityResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
effective_from: Optional[datetime] = # Replace with your value
as_at: datetime = # Replace with your value
links: Optional[List[Link]] = None
deleted_entity_response_instance = DeletedEntityResponse(href=href, effective_from=effective_from, as_at=as_at, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

