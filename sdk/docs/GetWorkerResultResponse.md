# GetWorkerResultResponse

The RunWorker response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**worker_status** | **str** | The final status of the Worker | 
**results** | **List[Dict[str, object]]** | Results | 
**status_detail** | **str** | Detail on the final status | [optional] 

## Example

```python
from lusid_workflow.models.get_worker_result_response import GetWorkerResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkerResultResponse from a JSON string
get_worker_result_response_instance = GetWorkerResultResponse.from_json(json)
# print the JSON string representation of the object
print GetWorkerResultResponse.to_json()

# convert the object into a dict
get_worker_result_response_dict = get_worker_result_response_instance.to_dict()
# create an instance of GetWorkerResultResponse from a dict
get_worker_result_response_form_dict = get_worker_result_response.from_dict(get_worker_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


