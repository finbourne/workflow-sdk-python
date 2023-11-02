# WorkerStatusTriggers

Defines triggers that will be invoked per Worker outcome

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started** | **str** | Trigger to invoke when the Worker has Started | [optional] 
**completed_with_results** | **str** | Trigger to invoke when the Worker has Completed (with results) | [optional] 
**completed_no_results** | **str** | Trigger to invoke when the Worker has Completed (no results) | [optional] 
**failed_to_start** | **str** | Trigger to invoke when the Worker has Failed to Start | [optional] 
**failed_to_complete** | **str** | Trigger to invoke when the Worker has Failed to Complete | [optional] 

## Example

```python
from lusid_workflow.models.worker_status_triggers import WorkerStatusTriggers

# TODO update the JSON string below
json = "{}"
# create an instance of WorkerStatusTriggers from a JSON string
worker_status_triggers_instance = WorkerStatusTriggers.from_json(json)
# print the JSON string representation of the object
print WorkerStatusTriggers.to_json()

# convert the object into a dict
worker_status_triggers_dict = worker_status_triggers_instance.to_dict()
# create an instance of WorkerStatusTriggers from a dict
worker_status_triggers_form_dict = worker_status_triggers.from_dict(worker_status_triggers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


