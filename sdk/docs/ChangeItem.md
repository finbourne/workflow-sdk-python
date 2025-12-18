# ChangeItem

Defines a change that occured to a Task
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_modified** | **datetime** | The AsAt time of the change | 
**user_id_modified** | **str** | The User ID that performed the change | 
**request_id_modified** | **str** | The Request ID of the request that caused the change | 
**as_at_version_number** | **int** | The AsAt Version number | 
**action** | **str** | The Action that resulted in the change | 
**attribute_name** | **str** | The name of the attribute that has been change | 
**previous_value** | **object** | The value of the attribute prior to the change | [optional] 
**new_value** | **object** | The value of the attribute following the change | 
## Example

```python
from lusid_workflow.models.change_item import ChangeItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at_modified: datetime = # Replace with your value
user_id_modified: StrictStr = "example_user_id_modified"
request_id_modified: StrictStr = "example_request_id_modified"
as_at_version_number: StrictInt = # Replace with your value
as_at_version_number: StrictInt = 42
action: StrictStr = "example_action"
attribute_name: StrictStr = "example_attribute_name"
previous_value: Optional[Any] = # Replace with your value
new_value: Optional[Any] = # Replace with your value
change_item_instance = ChangeItem(as_at_modified=as_at_modified, user_id_modified=user_id_modified, request_id_modified=request_id_modified, as_at_version_number=as_at_version_number, action=action, attribute_name=attribute_name, previous_value=previous_value, new_value=new_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

