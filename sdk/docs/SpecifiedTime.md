# SpecifiedTime

A specified time in the day

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hours** | **int** | Hours | 
**minutes** | **int** | Minutes | 
**type** | **str** | The type of Time of Day | 

## Example

```python
from lusid_workflow.models.specified_time import SpecifiedTime

# TODO update the JSON string below
json = "{}"
# create an instance of SpecifiedTime from a JSON string
specified_time_instance = SpecifiedTime.from_json(json)
# print the JSON string representation of the object
print SpecifiedTime.to_json()

# convert the object into a dict
specified_time_dict = specified_time_instance.to_dict()
# create an instance of SpecifiedTime from a dict
specified_time_form_dict = specified_time.from_dict(specified_time_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


