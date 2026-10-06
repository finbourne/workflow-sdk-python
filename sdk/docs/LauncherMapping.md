# LauncherMapping

A value a Launcher either gives as it is or takes from somewhere.              Exactly one of Finbourne.Workflow.WebApi.Common.Dto.Json.Launchers.LauncherMapping.SetTo or Finbourne.Workflow.WebApi.Common.Dto.Json.Launchers.LauncherMapping.MapFrom must be given. Only an Event Launcher has an event to take a value from, so a Schedule Launcher can only use Finbourne.Workflow.WebApi.Common.Dto.Json.Launchers.LauncherMapping.SetTo
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set_to** | **str** | The value to use, given as it is | [optional] 
**map_from** | **str** | The path the value is taken from, for example header.userId | [optional] 
## Example

```python
from lusid_workflow.models.launcher_mapping import LauncherMapping
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

set_to: Optional[StrictStr] = "example_set_to"
map_from: Optional[StrictStr] = "example_map_from"
launcher_mapping_instance = LauncherMapping(set_to=set_to, map_from=map_from)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

