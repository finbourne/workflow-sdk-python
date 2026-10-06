# ResultsNotRecurringConfiguration

Behaviour applied when a new child task candidate's stacking key does not match any existing (non-terminal) child task, and to an existing child task whose stacking key is not matched by any new candidate
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing_tasks** | [**ExistingTasksNotRecurringConfiguration**](ExistingTasksNotRecurringConfiguration.md) |  | 
## Example

```python
from lusid_workflow.models.results_not_recurring_configuration import ResultsNotRecurringConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

existing_tasks: ExistingTasksNotRecurringConfiguration = # Replace with your value
results_not_recurring_configuration_instance = ResultsNotRecurringConfiguration(existing_tasks=existing_tasks)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

