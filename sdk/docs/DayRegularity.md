# DayRegularity

Day Regularity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | The frequency of the Day Regularity | 
**type** | **str** | The type of Date Regularity | 

## Example

```python
from lusid_workflow.models.day_regularity import DayRegularity

# TODO update the JSON string below
json = "{}"
# create an instance of DayRegularity from a JSON string
day_regularity_instance = DayRegularity.from_json(json)
# print the JSON string representation of the object
print DayRegularity.to_json()

# convert the object into a dict
day_regularity_dict = day_regularity_instance.to_dict()
# create an instance of DayRegularity from a dict
day_regularity_form_dict = day_regularity.from_dict(day_regularity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


