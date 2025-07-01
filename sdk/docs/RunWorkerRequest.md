# RunWorkerRequest

Request to Create a new worker
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**List[ParameterValue]**](ParameterValue.md) | The Parameter and their values. | 
**worker_timeout** | **int** | The timeout in seconds for the worker | [optional] 
## Example

```python
from lusid_workflow.models.run_worker_request import RunWorkerRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, conlist

parameters: conlist(ParameterValue) = # Replace with your value
worker_timeout: Optional[StrictInt] = # Replace with your value
worker_timeout: Optional[StrictInt] = None
run_worker_request_instance = RunWorkerRequest(parameters=parameters, worker_timeout=worker_timeout)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

