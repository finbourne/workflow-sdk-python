# WorkflowResponse

A Workflow
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**version** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**root_task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**workflow_structure** | [**WorkflowStructure**](WorkflowStructure.md) |  | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The properties of the Workflow, keyed by property key. | [optional] 
## Example

```python
from lusid_workflow.models.workflow_response import WorkflowResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
version: Optional[VersionInfo] = None
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
root_task_definition_id: ResourceId = # Replace with your value
workflow_structure: Optional[WorkflowStructure] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
workflow_response_instance = WorkflowResponse(id=id, version=version, display_name=display_name, description=description, root_task_definition_id=root_task_definition_id, workflow_structure=workflow_structure, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

