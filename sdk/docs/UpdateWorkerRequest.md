# UpdateWorkerRequest

Request to Update a new worker
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**worker_configuration** | **object** | Information about how the worker should be executed | 
## Example

```python
from lusid_workflow.models.update_worker_request import UpdateWorkerRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
worker_configuration: Optional[Any] = # Replace with your value
update_worker_request_instance = UpdateWorkerRequest(display_name=display_name, description=description, worker_configuration=worker_configuration)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

