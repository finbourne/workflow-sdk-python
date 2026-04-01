# CreateWorkflowRequest

Contains required info to create a new Workflow
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**root_task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
## Example

```python
from lusid_workflow.models.create_workflow_request import CreateWorkflowRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
root_task_definition_id: ResourceId = # Replace with your value
create_workflow_request_instance = CreateWorkflowRequest(id=id, display_name=display_name, description=description, root_task_definition_id=root_task_definition_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

