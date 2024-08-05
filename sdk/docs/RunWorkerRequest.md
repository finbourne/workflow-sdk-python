# RunWorkerRequest

Request to Create a new worker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**List[ParameterValue]**](ParameterValue.md) | The Parameter and their values. | 

## Example

```python
from lusid_workflow.models.run_worker_request import RunWorkerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunWorkerRequest from a JSON string
run_worker_request_instance = RunWorkerRequest.from_json(json)
# print the JSON string representation of the object
print RunWorkerRequest.to_json()

# convert the object into a dict
run_worker_request_dict = run_worker_request_instance.to_dict()
# create an instance of RunWorkerRequest from a dict
run_worker_request_form_dict = run_worker_request.from_dict(run_worker_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


