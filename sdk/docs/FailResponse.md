# FailResponse

Readonly configuration for a Worker that always Fails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | [optional] 

## Example

```python
from lusid_workflow.models.fail_response import FailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FailResponse from a JSON string
fail_response_instance = FailResponse.from_json(json)
# print the JSON string representation of the object
print FailResponse.to_json()

# convert the object into a dict
fail_response_dict = fail_response_instance.to_dict()
# create an instance of FailResponse from a dict
fail_response_form_dict = fail_response.from_dict(fail_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


