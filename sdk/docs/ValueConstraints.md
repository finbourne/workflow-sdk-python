# ValueConstraints

Constraints that should be applied to a Tasks fields
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraint_type** | **str** | Whether the constraint is a suggestion or should be enforced via validation (e.g. Suggested, Validated) | 
**value_source_type** | **str** | The source of the acceptable values (e.g. AcceptableValues) | 
**acceptable_values** | **List[object]** | The acceptable values for the field | 
## Example

```python
from lusid_workflow.models.value_constraints import ValueConstraints
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

constraint_type: StrictStr = "example_constraint_type"
value_source_type: StrictStr = "example_value_source_type"
acceptable_values: List[Any] = # Replace with your value
value_constraints_instance = ValueConstraints(constraint_type=constraint_type, value_source_type=value_source_type, acceptable_values=acceptable_values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

