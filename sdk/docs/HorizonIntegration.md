# HorizonIntegration

Configuration for a Worker that executes a Horizon integration instance
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | 
**integration_instance_id** | **str** | The id of the Horizon integration instance the worker executes. | 
## Example

```python
from lusid_workflow.models.horizon_integration import HorizonIntegration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
integration_instance_id: StrictStr = "example_integration_instance_id"
horizon_integration_instance = HorizonIntegration(type=type, integration_instance_id=integration_instance_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

