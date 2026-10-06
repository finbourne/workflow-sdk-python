# CreateLauncherRequest

Contains information for creating a Launcher on a Workflow.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**launcher_id** | **str** | The identifier of the Launcher inside its Workflow | 
**display_name** | **str** | Human-readable name | 
**description** | **str** | Human-readable description | [optional] 
**status** | **str** | The current status of the Launcher. One of - Active, Inactive | 
**launcher_details** | [**LauncherDetails**](LauncherDetails.md) |  | 
## Example

```python
from lusid_workflow.models.create_launcher_request import CreateLauncherRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

launcher_id: StrictStr = "example_launcher_id"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
status: StrictStr = "example_status"
launcher_details: LauncherDetails = # Replace with your value
create_launcher_request_instance = CreateLauncherRequest(launcher_id=launcher_id, display_name=display_name, description=description, status=status, launcher_details=launcher_details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

