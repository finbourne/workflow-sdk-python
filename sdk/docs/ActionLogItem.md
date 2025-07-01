# ActionLogItem

A log item for a given Action Log
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The timestamp of the log item | 
**log_type** | **str** | The type of log item | 
**details** | **str** | The details of the log item | [optional] 
## Example

```python
from lusid_workflow.models.action_log_item import ActionLogItem
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr
from datetime import datetime
timestamp: datetime = # Replace with your value
log_type: StrictStr = "example_log_type"
details: Optional[StrictStr] = "example_details"
action_log_item_instance = ActionLogItem(timestamp=timestamp, log_type=log_type, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

