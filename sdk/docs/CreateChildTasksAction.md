# CreateChildTasksAction

Defines a Create Child Tasks Action
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | 
**child_task_configurations** | [**List[CreateChildTaskConfiguration]**](CreateChildTaskConfiguration.md) | The Child Task Configurations | 
## Example

```python
from lusid_workflow.models.create_child_tasks_action import CreateChildTasksAction
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

type: StrictStr = "example_type"
child_task_configurations: conlist(CreateChildTaskConfiguration) = # Replace with your value
create_child_tasks_action_instance = CreateChildTasksAction(type=type, child_task_configurations=child_task_configurations)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

