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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
worker_configuration: WorkerConfigurationResponse = # Replace with your value
version: Optional[VersionInfo] = None
parameters: Optional[List[Parameter]] = # Replace with your value
result_fields: Optional[List[ResultField]] = # Replace with your value
links: Optional[List[Link]] = None
worker_instance = Worker(id=id, display_name=display_name, description=description, worker_configuration=worker_configuration, version=version, parameters=parameters, result_fields=result_fields, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

