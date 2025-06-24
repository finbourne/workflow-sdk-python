# WeekRegularity

Week Regularity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | The frequency of the Week Regularity | 
**days_of_week** | **List[str]** | Days of the week | 
**type** | **str** | The type of Date Regularity | 

## Example

```python
from lusid_workflow.models.week_regularity import WeekRegularity

# TODO update the JSON string below
json = "{}"
# create an instance of WeekRegularity from a JSON string
week_regularity_instance = WeekRegularity.from_json(json)
# print the JSON string representation of the object
print WeekRegularity.to_json()

# convert the object into a dict
week_regularity_dict = week_regularity_instance.to_dict()
# create an instance of WeekRegularity from a dict
week_regularity_form_dict = week_regularity.from_dict(week_regularity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


