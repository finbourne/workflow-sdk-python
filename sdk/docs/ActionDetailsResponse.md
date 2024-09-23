# ActionDetailsResponse

Abstracts the kinds of Actions available in a read-only form

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | [optional] 
**child_task_configurations** | [**List[ResultantChildTaskConfiguration]**](ResultantChildTaskConfiguration.md) | Tasks can be generated from run worker results; this is the configuration | [optional] 
**worker_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**worker_as_at** | **datetime** | Worker AsAt | [optional] 
**worker_parameters** | [**Dict[str, FieldMapping]**](FieldMapping.md) | Parameters for this Worker | [optional] 
**worker_status_triggers** | [**WorkerStatusTriggers**](WorkerStatusTriggers.md) |  | [optional] 
**worker_timeout** | **int** | Worker timeout in seconds | [optional] 
**trigger** | **str** | Trigger on parent task to be invoked | [optional] 

## Example

```python
from lusid_workflow.models.action_details_response import ActionDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionDetailsResponse from a JSON string
action_details_response_instance = ActionDetailsResponse.from_json(json)
# print the JSON string representation of the object
print ActionDetailsResponse.to_json()

# convert the object into a dict
action_details_response_dict = action_details_response_instance.to_dict()
# create an instance of ActionDetailsResponse from a dict
action_details_response_form_dict = action_details_response.from_dict(action_details_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


