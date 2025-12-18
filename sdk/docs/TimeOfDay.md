# TimeOfDay

A time of the day
## Example

```python
from lusid_workflow.models.time_of_day import TimeOfDay
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

# Example with TimeOfDay 

cut_label_reference_instance = lusid_workflow.models.cut_label_reference.CutLabelReference(
                        code = 'z', 
                        type = 'CutLabel', )

time_of_day_instance = TimeOfDay(cut_label_reference_instance)

```
See all compatible oneOf types with TimeOfDay


 * [SpecifiedTime](./SpecifiedTime.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

