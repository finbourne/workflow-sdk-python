# Sleep

Configuration for a Worker that Sleeps for a user-defined amount of time
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | 
## Example

```python
from lusid_workflow.models.sleep import Sleep
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

type: StrictStr = "example_type"
sleep_instance = Sleep(type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

