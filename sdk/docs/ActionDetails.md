# ActionDetails

Abstracts the kinds of Actions available

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | 
**child_task_configurations** | [**List[ResultantChildTaskConfiguration]**](ResultantChildTaskConfiguration.md) | Tasks can be generated from run worker results; this is the configuration | 
**worker_id** | [**ResourceId**](ResourceId.md) |  | 
**worker_as_at** | **datetime** | Worker AsAt | [optional] 
**worker_parameters** | [**Dict[str, FieldMapping]**](FieldMapping.md) | Parameters for this Worker | [optional] 
**worker_status_triggers** | [**WorkerStatusTriggers**](WorkerStatusTriggers.md) |  | [optional] 
**trigger** | **str** | Trigger on parent task to be invoked | 

## Example

```python
from lusid_workflow.models.action_details import ActionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ActionDetails from a JSON string
action_details_instance = ActionDetails.from_json(json)
# print the JSON string representation of the object
print ActionDetails.to_json()

# convert the object into a dict
action_details_dict = action_details_instance.to_dict()
# create an instance of ActionDetails from a dict
action_details_form_dict = action_details.from_dict(action_details_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


