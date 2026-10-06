# ExistingTasksNotRecurringConfiguration

Behaviour applied to an existing (non-terminal) child task whose stacking key is not matched by any new child task candidate (i.e. it did not recur on this run)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger** | **str** | The existing task receives this trigger | [optional] 
## Example

```python
from lusid_workflow.models.existing_tasks_not_recurring_configuration import ExistingTasksNotRecurringConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

trigger: Optional[StrictStr] = "example_trigger"
existing_tasks_not_recurring_configuration_instance = ExistingTasksNotRecurringConfiguration(trigger=trigger)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

