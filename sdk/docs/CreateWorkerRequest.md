# CreateWorkerRequest

Request to Create a new worker
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**worker_configuration** | [**WorkerConfiguration**](WorkerConfiguration.md) |  | 
## Example

```python
from lusid_workflow.models.create_worker_request import CreateWorkerRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

id: ResourceId = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
worker_configuration: WorkerConfiguration = # Replace with your value
create_worker_request_instance = CreateWorkerRequest(id=id, display_name=display_name, description=description, worker_configuration=worker_configuration)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

