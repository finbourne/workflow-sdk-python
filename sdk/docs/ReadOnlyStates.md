# ReadOnlyStates

Information about which states the field can be edited in
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_type** | **str** | The State Type (e.g. InitialState, AllStates, TerminalState, SelectedStates) | 
**selected_states** | **List[str]** | Named states for which the field will be readonly - This field can only be populated if StateType &#x3D; SelectedStates | [optional] 
## Example

```python
from lusid_workflow.models.read_only_states import ReadOnlyStates
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

state_type: StrictStr = "example_state_type"
selected_states: Optional[List[StrictStr]] = # Replace with your value
read_only_states_instance = ReadOnlyStates(state_type=state_type, selected_states=selected_states)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

