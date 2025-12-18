# ActionLogOrigin

The Action Log Origin contains information about how the Action was created
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | The Id of the Task that created this Action | [optional] 
**request_id** | **str** | The request Id of the request that caused this Action to be triggered. This could be the original request that caused a sequence of Actions that resulted in this Action | 
## Example

```python
from lusid_workflow.models.action_log_origin import ActionLogOrigin
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

task_id: Optional[StrictStr] = "example_task_id"
request_id: StrictStr = "example_request_id"
action_log_origin_instance = ActionLogOrigin(task_id=task_id, request_id=request_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

