# CorrelationIdMapping

How an Event Launcher fills one correlation ID of the root task from the event that arrived.              A mapped correlation ID joins the fixed correlation IDs of the Launcher
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map_from** | **str** | The path into the event the correlation ID is taken from, for example body.fileId | 
## Example

```python
from lusid_workflow.models.correlation_id_mapping import CorrelationIdMapping
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

map_from: StrictStr = "example_map_from"
correlation_id_mapping_instance = CorrelationIdMapping(map_from=map_from)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

