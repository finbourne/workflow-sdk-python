# WorkerConfigurationResponse

Readonly information about how the worker should be executed
## Example

```python
from lusid_workflow.models.worker_configuration_response import WorkerConfigurationResponse
from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator

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

