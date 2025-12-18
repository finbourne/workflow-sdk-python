# UpdateTaskWithIdAndTriggerRequest

A request to update multiple Tasks Includes a trigger which is supplied from route in single update request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_instance_id** | **str** | The ID of the task instance | [optional] 
**correlation_ids** | **List[str]** | A set of guid identifiers that allow correlation across the application tier | [optional] 
**fields** | [**List[TaskInstanceField]**](TaskInstanceField.md) | Defines the fields associated with the update | [optional] 
**stacking_key** | **str** | The key for the Stack that this Task should be added to | [optional] 
**trigger_name** | **str** | The trigger we want to update the task with | [optional] 
## Example

```python
from lusid_workflow.models.update_task_with_id_and_trigger_request import UpdateTaskWithIdAndTriggerRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

task_instance_id: Optional[StrictStr] = "example_task_instance_id"
correlation_ids: Optional[List[StrictStr]] = # Replace with your value
fields: Optional[List[TaskInstanceField]] = # Replace with your value
stacking_key: Optional[StrictStr] = "example_stacking_key"
trigger_name: Optional[StrictStr] = "example_trigger_name"
update_task_with_id_and_trigger_request_instance = UpdateTaskWithIdAndTriggerRequest(task_instance_id=task_instance_id, correlation_ids=correlation_ids, fields=fields, stacking_key=stacking_key, trigger_name=trigger_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

