# EventHandlerMapping

Defines a mapping for event handler properties
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map_from** | **str** | The field to map from | [optional] 
**set_to** | **str** | The (constant) value to set | [optional] 
## Example

```python
from lusid_workflow.models.event_handler_mapping import EventHandlerMapping
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

map_from: Optional[StrictStr] = "example_map_from"
set_to: Optional[StrictStr] = "example_set_to"
event_handler_mapping_instance = EventHandlerMapping(map_from=map_from, set_to=set_to)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

