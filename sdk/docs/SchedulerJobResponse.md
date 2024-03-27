# SchedulerJobResponse

Readonly configuration for a Worker that calls a Scheduler job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | [optional] 
**job_id** | [**ResourceId**](ResourceId.md) |  | [optional] 

## Example

```python
from lusid_workflow.models.scheduler_job_response import SchedulerJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulerJobResponse from a JSON string
scheduler_job_response_instance = SchedulerJobResponse.from_json(json)
# print the JSON string representation of the object
print SchedulerJobResponse.to_json()

# convert the object into a dict
scheduler_job_response_dict = scheduler_job_response_instance.to_dict()
# create an instance of SchedulerJobResponse from a dict
scheduler_job_response_form_dict = scheduler_job_response.from_dict(scheduler_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


