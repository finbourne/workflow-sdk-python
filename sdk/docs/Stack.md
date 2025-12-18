# Stack

Information pertaining to the Tasks Stack if one is present
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_added_as_at** | **datetime** | When the Task was added to the Stack | [optional] 
**stack_opened_as_at** | **datetime** | When the Stack was opened | [optional] 
**stack_closed_as_at** | **datetime** | When the Stack was closed | [optional] 
**stack_membership_type** | **str** | Whether the task is the Lead task of the Stack or a Member within the Stack | [optional] 
**stack_status** | **str** | Status of the Stack (Open/Closed) | [optional] 
**lead_task_id** | **str** | ID of the Lead Task | [optional] 
**lead_task_state** | **str** | State of the Lead Task | [optional] 
**tasks_in_stack** | **int** | Number of Tasks in the Stack | [optional] 
## Example

```python
from lusid_workflow.models.stack import Stack
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

member_added_as_at: Optional[datetime] = # Replace with your value
stack_opened_as_at: Optional[datetime] = # Replace with your value
stack_closed_as_at: Optional[datetime] = # Replace with your value
stack_membership_type: Optional[StrictStr] = "example_stack_membership_type"
stack_status: Optional[StrictStr] = "example_stack_status"
lead_task_id: Optional[StrictStr] = "example_lead_task_id"
lead_task_state: Optional[StrictStr] = "example_lead_task_state"
tasks_in_stack: Optional[StrictInt] = # Replace with your value
tasks_in_stack: Optional[StrictInt] = None
stack_instance = Stack(member_added_as_at=member_added_as_at, stack_opened_as_at=stack_opened_as_at, stack_closed_as_at=stack_closed_as_at, stack_membership_type=stack_membership_type, stack_status=stack_status, lead_task_id=lead_task_id, lead_task_state=lead_task_state, tasks_in_stack=tasks_in_stack)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

