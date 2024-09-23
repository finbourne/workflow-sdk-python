# RunWorkerActionResponse

Defines a read-only Run Worker Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | [optional] 
**worker_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**worker_as_at** | **datetime** | Worker AsAt | [optional] 
**worker_parameters** | [**Dict[str, FieldMapping]**](FieldMapping.md) | Parameters for this Worker | [optional] 
**worker_status_triggers** | [**WorkerStatusTriggers**](WorkerStatusTriggers.md) |  | [optional] 
**child_task_configurations** | [**List[ResultantChildTaskConfiguration]**](ResultantChildTaskConfiguration.md) | Tasks can be generated from run worker results; this is the configuration | [optional] 
**worker_timeout** | **int** | Worker timeout in seconds | [optional] 

## Example

```python
from lusid_workflow.models.run_worker_action_response import RunWorkerActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RunWorkerActionResponse from a JSON string
run_worker_action_response_instance = RunWorkerActionResponse.from_json(json)
# print the JSON string representation of the object
print RunWorkerActionResponse.to_json()

# convert the object into a dict
run_worker_action_response_dict = run_worker_action_response_instance.to_dict()
# create an instance of RunWorkerActionResponse from a dict
run_worker_action_response_form_dict = run_worker_action_response.from_dict(run_worker_action_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


