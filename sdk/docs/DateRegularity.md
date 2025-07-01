# DateRegularity

A Date Regularity
## Example

```python
from lusid_workflow.models.date_regularity import DateRegularity
from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator

# Example with DateRegularity 

day_regularity_instance = lusid_workflow.models.day_regularity.DayRegularity(
                        frequency = 1, 
                        type = '0', )

date_regularity_instance = DateRegularity(day_regularity_instance)

```
See all compatible oneOf types with DateRegularity


 * [RelativeMonthRegularity](./RelativeMonthRegularity.md)

 * [SpecificMonthRegularity](./SpecificMonthRegularity.md)

 * [WeekRegularity](./WeekRegularity.md)

 * [YearRegularity](./YearRegularity.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

