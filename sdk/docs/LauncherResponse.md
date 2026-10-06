# LauncherResponse

A Launcher, which starts a run of one Workflow either at the times a schedule gives or when a matching event arrives
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | [**ResourceId**](ResourceId.md) |  | 
**launcher_id** | **str** | The identifier of this Launcher inside its Workflow | 
**display_name** | **str** | Human-readable name | 
**description** | **str** | Human-readable description | [optional] 
**status** | **str** | The current status of the Launcher. One of - Active, Inactive | 
**launcher_details** | [**LauncherDetailsResponse**](LauncherDetailsResponse.md) |  | 
**summaries** | [**LauncherSummaries**](LauncherSummaries.md) |  | [optional] 
**version** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
## Example

```python
from lusid_workflow.models.launcher_response import LauncherResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

workflow_id: ResourceId = # Replace with your value
launcher_id: StrictStr = "example_launcher_id"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
status: StrictStr = "example_status"
launcher_details: LauncherDetailsResponse = # Replace with your value
summaries: Optional[LauncherSummaries] = None
version: Optional[VersionInfo] = None
launcher_response_instance = LauncherResponse(workflow_id=workflow_id, launcher_id=launcher_id, display_name=display_name, description=description, status=status, launcher_details=launcher_details, summaries=summaries, version=version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

