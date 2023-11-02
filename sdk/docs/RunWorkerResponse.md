# RunWorkerResponse

The RunWorker response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **int** | Identifies a Worker run | 
**status_detail** | **str** | Detail on the final status | [optional] 

## Example

```python
from lusid_workflow.models.run_worker_response import RunWorkerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RunWorkerResponse from a JSON string
run_worker_response_instance = RunWorkerResponse.from_json(json)
# print the JSON string representation of the object
print RunWorkerResponse.to_json()

# convert the object into a dict
run_worker_response_dict = run_worker_response_instance.to_dict()
# create an instance of RunWorkerResponse from a dict
run_worker_response_form_dict = run_worker_response.from_dict(run_worker_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


