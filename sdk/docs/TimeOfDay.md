# TimeOfDay

A time of the day
## Example

```python
from lusid_workflow.models.time_of_day import TimeOfDay
from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator

# Example with TimeOfDay 

cut_label_reference_instance = lusid_workflow.models.cut_label_reference.CutLabelReference(
                        code = 'z0', 
                        type = '0', )

time_of_day_instance = TimeOfDay(cut_label_reference_instance)

```
See all compatible oneOf types with TimeOfDay


 * [SpecifiedTime](./SpecifiedTime.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

