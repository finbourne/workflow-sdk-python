# LaunchedBy

The Launcher that started a run of a Workflow
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**launcher_id** | **str** | The ID of the Launcher inside its Workflow | 
**launcher_type** | **str** | The type of Launcher. One of - Schedule, Event | 
**launcher_as_at** | **datetime** | The version.asAtModified of the Launcher definition that fired | 
**fired_at** | **datetime** | When the Launcher fired. For a Schedule Launcher this is the scheduled trigger time, and for an Event Launcher it is the timestamp of the event | 
## Example

```python
from lusid_workflow.models.launched_by import LaunchedBy
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

launcher_id: StrictStr = "example_launcher_id"
launcher_type: StrictStr = "example_launcher_type"
launcher_as_at: datetime = # Replace with your value
fired_at: datetime = # Replace with your value
launched_by_instance = LaunchedBy(launcher_id=launcher_id, launcher_type=launcher_type, launcher_as_at=launcher_as_at, fired_at=fired_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

