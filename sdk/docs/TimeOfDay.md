# TimeOfDay

A time of the day

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of Time of Day | 
**code** | **str** | Code of the Cut Label | 
**hours** | **int** | Hours | 
**minutes** | **int** | Minutes | 

## Example

```python
from lusid_workflow.models.time_of_day import TimeOfDay

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOfDay from a JSON string
time_of_day_instance = TimeOfDay.from_json(json)
# print the JSON string representation of the object
print TimeOfDay.to_json()

# convert the object into a dict
time_of_day_dict = time_of_day_instance.to_dict()
# create an instance of TimeOfDay from a dict
time_of_day_form_dict = time_of_day.from_dict(time_of_day_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


