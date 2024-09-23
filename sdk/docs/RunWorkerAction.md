# RunWorkerAction

Defines a Run Worker Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | 
**worker_id** | [**ResourceId**](ResourceId.md) |  | 
**worker_as_at** | **datetime** | Worker AsAt | [optional] 
**worker_parameters** | [**Dict[str, FieldMapping]**](FieldMapping.md) | Parameters for this Worker | [optional] 
**worker_status_triggers** | [**WorkerStatusTriggers**](WorkerStatusTriggers.md) |  | [optional] 
**child_task_configurations** | [**List[ResultantChildTaskConfiguration]**](ResultantChildTaskConfiguration.md) | Tasks can be generated from run worker results; this is the configuration | [optional] 
**worker_timeout** | **int** | Worker WorkerTimeout in seconds | [optional] 

## Example

```python
from lusid_workflow.models.run_worker_action import RunWorkerAction

# TODO update the JSON string below
json = "{}"
# create an instance of RunWorkerAction from a JSON string
run_worker_action_instance = RunWorkerAction.from_json(json)
# print the JSON string representation of the object
print RunWorkerAction.to_json()

# convert the object into a dict
run_worker_action_dict = run_worker_action_instance.to_dict()
# create an instance of RunWorkerAction from a dict
run_worker_action_form_dict = run_worker_action.from_dict(run_worker_action_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


