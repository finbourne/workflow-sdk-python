# LauncherSummaries

Sentences that say what a Launcher does, meant to be shown to a person.              These are rendered on read from the stored Launcher details. They are never stored and never accepted on a write, so the same Launcher always reads back the same summaries
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | **str** | A sentence that says when the Launcher starts a run, for example \&quot;Weekly on Mon at 09:00, rolled forward to the next business day\&quot;.              Null for an Event Launcher, which has no schedule | [optional] 
**fields** | **Dict[str, Optional[str]]** | A sentence for each field of the root task the Launcher fills, keyed by the field name on the root task definition. Empty when the Launcher fills no fields | [optional] 
## Example

```python
from lusid_workflow.models.launcher_summaries import LauncherSummaries
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

schedule: Optional[StrictStr] = "example_schedule"
fields: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
launcher_summaries_instance = LauncherSummaries(schedule=schedule, fields=fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

