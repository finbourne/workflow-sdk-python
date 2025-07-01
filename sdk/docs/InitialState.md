# InitialState

Defines the Initial State of the Task
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Initial State of the Task | 
**required_fields** | **List[str]** | Required input Fields for the Initial State | [optional] 
## Example

```python
from lusid_workflow.models.initial_state import InitialState
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

name: StrictStr = "example_name"
required_fields: Optional[conlist(StrictStr)] = # Replace with your value
initial_state_instance = InitialState(name=name, required_fields=required_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

