# Worker

Information about the Worker
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**worker_configuration** | [**WorkerConfigurationResponse**](WorkerConfigurationResponse.md) |  | 
**version** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
**parameters** | [**List[Parameter]**](Parameter.md) | The Parameters this Worker accepts or requires. | [optional] 
**result_fields** | [**List[ResultField]**](ResultField.md) | The Fields that the Worker results will come back with. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid_workflow.models.worker import Worker
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

id: ResourceId = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
worker_configuration: WorkerConfigurationResponse = # Replace with your value
version: Optional[VersionInfo] = None
parameters: Optional[conlist(Parameter)] = # Replace with your value
result_fields: Optional[conlist(ResultField)] = # Replace with your value
links: Optional[conlist(Link)] = None
worker_instance = Worker(id=id, display_name=display_name, description=description, worker_configuration=worker_configuration, version=version, parameters=parameters, result_fields=result_fields, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

