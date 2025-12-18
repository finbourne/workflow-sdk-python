# HealthCheckResponse

Readonly configuration for a Worker that performs a GET against a given Url.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | [optional] 
**url** | **str** | The URL to check, eg: https://www.google.com/ | [optional] 
## Example

```python
from lusid_workflow.models.health_check_response import HealthCheckResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
url: Optional[StrictStr] = "example_url"
health_check_response_instance = HealthCheckResponse(type=type, url=url)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

