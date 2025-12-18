# VersionInfo

The version metadata.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_created** | **datetime** | The asAt datetime at which this entity was first created. | [optional] 
**user_id_created** | **str** | The unique id of the user who created this entity. | [optional] 
**request_id_created** | **str** | The request id of the request that created this entity. | [optional] 
**as_at_modified** | **datetime** | The asAt datetime at which this entity was last updated. | [optional] 
**user_id_modified** | **str** | The unique id of the user who last updated this entity. | [optional] 
**request_id_modified** | **str** | The request id of the request that last updated this entity. | [optional] 
**as_at_version_number** | **int** | The integer version number for this entity (the entity was created at version 1). | [optional] 
## Example

```python
from lusid_workflow.models.version_info import VersionInfo
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at_created: Optional[datetime] = # Replace with your value
user_id_created: Optional[StrictStr] = "example_user_id_created"
request_id_created: Optional[StrictStr] = "example_request_id_created"
as_at_modified: Optional[datetime] = # Replace with your value
user_id_modified: Optional[StrictStr] = "example_user_id_modified"
request_id_modified: Optional[StrictStr] = "example_request_id_modified"
as_at_version_number: Optional[StrictInt] = # Replace with your value
as_at_version_number: Optional[StrictInt] = None
version_info_instance = VersionInfo(as_at_created=as_at_created, user_id_created=user_id_created, request_id_created=request_id_created, as_at_modified=as_at_modified, user_id_modified=user_id_modified, request_id_modified=request_id_modified, as_at_version_number=as_at_version_number)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

