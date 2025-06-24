# DateRegularity

A Date Regularity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of Date Regularity | 
**frequency** | **int** | The frequency of the Week Regularity | 
**days_of_week** | **List[str]** | Days of the week | 
**index** | **str** | Relative index in the month | 
**days_of_month** | **List[int]** | Days of the month | 
**dates** | [**List[DayOfYear]**](DayOfYear.md) | The dates in the year | 

## Example

```python
from lusid_workflow.models.date_regularity import DateRegularity

# TODO update the JSON string below
json = "{}"
# create an instance of DateRegularity from a JSON string
date_regularity_instance = DateRegularity.from_json(json)
# print the JSON string representation of the object
print DateRegularity.to_json()

# convert the object into a dict
date_regularity_dict = date_regularity_instance.to_dict()
# create an instance of DateRegularity from a dict
date_regularity_form_dict = date_regularity.from_dict(date_regularity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


