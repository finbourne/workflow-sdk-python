# SchedulerJob

Configuration for a Worker that calls a Scheduler Job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | 
**job_id** | [**ResourceId**](ResourceId.md) |  | 

## Example

```python
from lusid_workflow.models.scheduler_job import SchedulerJob

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulerJob from a JSON string
scheduler_job_instance = SchedulerJob.from_json(json)
# print the JSON string representation of the object
print SchedulerJob.to_json()

# convert the object into a dict
scheduler_job_dict = scheduler_job_instance.to_dict()
# create an instance of SchedulerJob from a dict
scheduler_job_form_dict = scheduler_job.from_dict(scheduler_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


