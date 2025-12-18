# WorkerConfigurationResponse

Readonly information about how the worker should be executed
## Example

```python
from lusid_workflow.models.worker_configuration_response import WorkerConfigurationResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

# Example with WorkerConfigurationResponse 

fail_response_instance = lusid_workflow.models.fail_response.FailResponse(
                        type = 'Fail', )

worker_configuration_response_instance = WorkerConfigurationResponse(fail_response_instance)

```
See all compatible oneOf types with WorkerConfigurationResponse


 * [GroupReconciliationResponse](./GroupReconciliationResponse.md)

 * [HealthCheckResponse](./HealthCheckResponse.md)

 * [LibraryResponse](./LibraryResponse.md)

 * [LuminesceViewResponse](./LuminesceViewResponse.md)

 * [SchedulerJobResponse](./SchedulerJobResponse.md)

 * [SleepResponse](./SleepResponse.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

