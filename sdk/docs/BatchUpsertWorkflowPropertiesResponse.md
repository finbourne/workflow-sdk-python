# BatchUpsertWorkflowPropertiesResponse

The result of a batch upsert of properties on a Workflow.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The properties that were successfully upserted or deleted, keyed by property key. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The properties that could not be upserted or deleted, keyed by property key. | [optional] 
**as_at_date** | **datetime** | The asAt datetime at which the properties were updated or created. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid_workflow.models.batch_upsert_workflow_properties_response import BatchUpsertWorkflowPropertiesResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
as_at_date: Optional[datetime] = # Replace with your value
links: Optional[List[Link]] = None
batch_upsert_workflow_properties_response_instance = BatchUpsertWorkflowPropertiesResponse(values=values, failed=failed, as_at_date=as_at_date, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

