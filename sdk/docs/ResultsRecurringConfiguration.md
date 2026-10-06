# ResultsRecurringConfiguration

Behaviour applied to new child task candidates, and to existing child tasks, when their stacking keys match one another
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_tasks** | [**NewTasksRecurringConfiguration**](NewTasksRecurringConfiguration.md) |  | 
**existing_tasks** | [**ExistingTasksRecurringConfiguration**](ExistingTasksRecurringConfiguration.md) |  | 
## Example

```python
from lusid_workflow.models.results_recurring_configuration import ResultsRecurringConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

new_tasks: NewTasksRecurringConfiguration = # Replace with your value
existing_tasks: ExistingTasksRecurringConfiguration = # Replace with your value
results_recurring_configuration_instance = ResultsRecurringConfiguration(new_tasks=new_tasks, existing_tasks=existing_tasks)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

