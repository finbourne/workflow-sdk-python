# ResultMatchingPattern

Standard Finbourne filter to match against Run Worker results

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Filter string | 

## Example

```python
from lusid_workflow.models.result_matching_pattern import ResultMatchingPattern

# TODO update the JSON string below
json = "{}"
# create an instance of ResultMatchingPattern from a JSON string
result_matching_pattern_instance = ResultMatchingPattern.from_json(json)
# print the JSON string representation of the object
print ResultMatchingPattern.to_json()

# convert the object into a dict
result_matching_pattern_dict = result_matching_pattern_instance.to_dict()
# create an instance of ResultMatchingPattern from a dict
result_matching_pattern_form_dict = result_matching_pattern.from_dict(result_matching_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


