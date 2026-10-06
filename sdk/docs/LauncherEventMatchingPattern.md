# LauncherEventMatchingPattern

Which events make an Event Launcher start a run of its Workflow
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The type of event to listen for. The list of available event types can be discovered by calling the ListEventTypes API endpoint in the Notifications service. Note that event types published by the Workflow service itself are not supported as Launcher triggers, and giving one will be rejected. | 
**filter** | **str** | A filter on the event. See https://support.lusid.com/filtering-results-from-lusid for more information. An empty filter matches every event of the type | [optional] 
## Example

```python
from lusid_workflow.models.launcher_event_matching_pattern import LauncherEventMatchingPattern
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

event_type: StrictStr = "example_event_type"
filter: Optional[StrictStr] = "example_filter"
launcher_event_matching_pattern_instance = LauncherEventMatchingPattern(event_type=event_type, filter=filter)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

