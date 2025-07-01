# ResultMatchingPattern

Standard Finbourne filter to match against Run Worker results
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Filter string | 
## Example

```python
from lusid_workflow.models.result_matching_pattern import ResultMatchingPattern
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

filter: StrictStr = "example_filter"
result_matching_pattern_instance = ResultMatchingPattern(filter=filter)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

