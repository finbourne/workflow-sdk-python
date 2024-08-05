# SleepResponse

Configuration for a Worker that Sleeps for a user-defined amount of time

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | 

## Example

```python
from lusid_workflow.models.sleep_response import SleepResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SleepResponse from a JSON string
sleep_response_instance = SleepResponse.from_json(json)
# print the JSON string representation of the object
print SleepResponse.to_json()

# convert the object into a dict
sleep_response_dict = sleep_response_instance.to_dict()
# create an instance of SleepResponse from a dict
sleep_response_form_dict = sleep_response.from_dict(sleep_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


