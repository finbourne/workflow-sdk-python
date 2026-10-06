# ReRunConfiguration

Defines how re-run results for a given (child) TaskDefinitionId should be reconciled against existing (non-terminal) child tasks of the same parent Task instance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**results_recurring** | [**ResultsRecurringConfiguration**](ResultsRecurringConfiguration.md) |  | 
**results_not_recurring** | [**ResultsNotRecurringConfiguration**](ResultsNotRecurringConfiguration.md) |  | 
## Example

```python
from lusid_workflow.models.re_run_configuration import ReRunConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

task_definition_id: ResourceId = # Replace with your value
results_recurring: ResultsRecurringConfiguration = # Replace with your value
results_not_recurring: ResultsNotRecurringConfiguration = # Replace with your value
re_run_configuration_instance = ReRunConfiguration(task_definition_id=task_definition_id, results_recurring=results_recurring, results_not_recurring=results_not_recurring)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

