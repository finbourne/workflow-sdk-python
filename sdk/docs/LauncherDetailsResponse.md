# LauncherDetailsResponse

What makes a Launcher start a run of its Workflow, and what it puts on the root task when it does, in a read only form.              The members here belong to every Launcher. Finbourne.Workflow.WebApi.Common.Dto.Json.Launchers.ScheduleLauncherDetailsResponse and Finbourne.Workflow.WebApi.Common.Dto.Json.Launchers.EventLauncherDetailsResponse add what only a schedule or only an event needs
## Example

```python
from lusid_workflow.models.launcher_details_response import LauncherDetailsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

# Example with LauncherDetailsResponse 

event_launcher_details_response_instance = lusid_workflow.models.event_launcher_details_response.EventLauncherDetailsResponse(
                        launcher_type = 'Event', 
                        event_matching_pattern = lusid_workflow.models.launcher_event_matching_pattern.LauncherEventMatchingPattern(
                            event_type = 'EiOTgswWMEJTcMoSLlNYUL', 
                            filter = '', ), 
                        map_task_fields = {
                            'key' : lusid_workflow.models.event_task_field_mapping.EventTaskFieldMapping(
                                map_from = '', 
                                date_time_adjustment = lusid_workflow.models.date_time_adjustment.DateTimeAdjustment(
                                    calendar_context = 'z', 
                                    date_adjustment = lusid_workflow.models.date_adjustment.DateAdjustment(
                                        delta_days = 56, 
                                        business_day_adjustment = '', ), 
                                    time_adjustment = lusid_workflow.models.time_adjustment.TimeAdjustment(
                                        set_to = lusid_workflow.models.specified_time.SpecifiedTime(
                                            hours = 56, 
                                            minutes = 56, 
                                            type = 'Specified', ), ), ), )
                            }, 
                        map_correlation_ids = [
                            lusid_workflow.models.correlation_id_mapping.CorrelationIdMapping(
                                map_from = '', )
                            ], 
                        run_as_user_id = lusid_workflow.models.launcher_mapping.LauncherMapping(
                            map_from = '', ), 
                        set_task_fields = {
                            'key' : null
                            }, 
                        set_correlation_ids = [
                            ''
                            ], 
                        initial_trigger = '', )

launcher_details_response_instance = LauncherDetailsResponse(event_launcher_details_response_instance)

```
See all compatible oneOf types with LauncherDetailsResponse


 * [ScheduleLauncherDetailsResponse](./ScheduleLauncherDetailsResponse.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

