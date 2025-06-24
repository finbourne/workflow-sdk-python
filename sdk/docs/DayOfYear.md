# DayOfYear

A day in the year

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **int** | Month in the year | 
**day** | **int** | Day in the month | 

## Example

```python
from lusid_workflow.models.day_of_year import DayOfYear

# TODO update the JSON string below
json = "{}"
# create an instance of DayOfYear from a JSON string
day_of_year_instance = DayOfYear.from_json(json)
# print the JSON string representation of the object
print DayOfYear.to_json()

# convert the object into a dict
day_of_year_dict = day_of_year_instance.to_dict()
# create an instance of DayOfYear from a dict
day_of_year_form_dict = day_of_year.from_dict(day_of_year_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


