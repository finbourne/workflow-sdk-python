# EventLauncherDetailsResponse

A read only Event Launcher, which starts a run of its Workflow when a matching platform event arrives
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**launcher_type** | **str** |  | [optional] 
**event_matching_pattern** | [**LauncherEventMatchingPattern**](LauncherEventMatchingPattern.md) |  | [optional] 
**map_task_fields** | [**Dict[str, EventTaskFieldMapping]**](EventTaskFieldMapping.md) | Fields of the root task filled from the event, keyed by the field name on the root task definition | [optional] 
**map_correlation_ids** | [**List[CorrelationIdMapping]**](CorrelationIdMapping.md) | Correlation IDs of the root task filled from the event | [optional] 
**run_as_user_id** | [**LauncherMapping**](LauncherMapping.md) |  | [optional] 
**set_task_fields** | **Dict[str, Optional[object]]** | Fields of the root task set to a fixed value, keyed by the field name on the root task definition | [optional] 
**set_correlation_ids** | **List[str]** | Correlation IDs put on the root task as given | [optional] 
**initial_trigger** | **str** | The trigger given to the root task once it is made and all of its fields are filled, or null when the root task is left in its initial state | [optional] 
## Example

```python
from lusid_workflow.models.event_launcher_details_response import EventLauncherDetailsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

launcher_type: Optional[StrictStr] = "example_launcher_type"
event_matching_pattern: Optional[LauncherEventMatchingPattern] = # Replace with your value
map_task_fields: Optional[Dict[str, EventTaskFieldMapping]] = # Replace with your value
map_correlation_ids: Optional[List[CorrelationIdMapping]] = # Replace with your value
run_as_user_id: Optional[LauncherMapping] = # Replace with your value
set_task_fields: Optional[Dict[str, Any]] = # Replace with your value
set_correlation_ids: Optional[List[StrictStr]] = # Replace with your value
initial_trigger: Optional[StrictStr] = "example_initial_trigger"
event_launcher_details_response_instance = EventLauncherDetailsResponse(launcher_type=launcher_type, event_matching_pattern=event_matching_pattern, map_task_fields=map_task_fields, map_correlation_ids=map_correlation_ids, run_as_user_id=run_as_user_id, set_task_fields=set_task_fields, set_correlation_ids=set_correlation_ids, initial_trigger=initial_trigger)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

