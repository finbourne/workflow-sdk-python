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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
required_fields: Optional[List[StrictStr]] = # Replace with your value
initial_state_instance = InitialState(name=name, required_fields=required_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

