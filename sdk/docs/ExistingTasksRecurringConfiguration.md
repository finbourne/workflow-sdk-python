# ExistingTasksRecurringConfiguration

Behaviour applied to an existing (non-terminal) child task whose stacking key matches one or more new child task candidates
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**increment_as_at_modified** | **bool** | When true, the existing task&#39;s asAtModified is incremented even if no other change (Trigger or MergeFields) is applied | [optional] 
**trigger** | **str** | The existing task receives this trigger | [optional] 
**merge_fields** | **List[str]** | The named fields on the existing task are updated with the values from the latest run. Only applies where the new-to-existing stacking key cardinality is one-to-one or one-to-many; unspecified fields are untouched. Data will be merged in even if these fields are in a read-only state. | [optional] 
## Example

```python
from lusid_workflow.models.existing_tasks_recurring_configuration import ExistingTasksRecurringConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

increment_as_at_modified: Optional[StrictBool] = # Replace with your value
increment_as_at_modified:Optional[StrictBool] = None
trigger: Optional[StrictStr] = "example_trigger"
merge_fields: Optional[List[StrictStr]] = # Replace with your value
existing_tasks_recurring_configuration_instance = ExistingTasksRecurringConfiguration(increment_as_at_modified=increment_as_at_modified, trigger=trigger, merge_fields=merge_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

