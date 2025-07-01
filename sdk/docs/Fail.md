# Fail

Configuration for a Worker that always Fails
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | 
## Example

```python
from lusid_workflow.models.fail import Fail
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

type: StrictStr = "example_type"
fail_instance = Fail(type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

