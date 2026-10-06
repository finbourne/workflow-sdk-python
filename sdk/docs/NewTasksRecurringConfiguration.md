# NewTasksRecurringConfiguration

Behaviour applied to a new child task candidate whose stacking key matches an existing (non-terminal) child task
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**do_not_create** | **bool** | When true, the new child task will not be created | [optional] 
**initial_trigger_override** | **str** | When DoNotCreate is false, the new child task will be created with this trigger instead of the ChildTaskConfiguration&#39;s InitialTrigger | [optional] 
## Example

```python
from lusid_workflow.models.new_tasks_recurring_configuration import NewTasksRecurringConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

do_not_create: Optional[StrictBool] = # Replace with your value
do_not_create:Optional[StrictBool] = None
initial_trigger_override: Optional[StrictStr] = "example_initial_trigger_override"
new_tasks_recurring_configuration_instance = NewTasksRecurringConfiguration(do_not_create=do_not_create, initial_trigger_override=initial_trigger_override)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

