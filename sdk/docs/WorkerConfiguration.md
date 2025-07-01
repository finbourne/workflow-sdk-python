# WorkerConfiguration

Information about how the worker should be executed
## Example

```python
from lusid_workflow.models.worker_configuration import WorkerConfiguration
from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator

# Example with WorkerConfiguration 

fail_instance = lusid_workflow.models.fail.Fail(
                        type = 'Fail', )

worker_configuration_instance = WorkerConfiguration(fail_instance)

```
See all compatible oneOf types with WorkerConfiguration


 * [GroupReconciliation](./GroupReconciliation.md)

 * [HealthCheck](./HealthCheck.md)

 * [LuminesceView](./LuminesceView.md)

 * [SchedulerJob](./SchedulerJob.md)

 * [Sleep](./Sleep.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

