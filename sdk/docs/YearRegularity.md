# YearRegularity

Year Regularity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dates** | [**List[DayOfYear]**](DayOfYear.md) | The dates in the year | 
**type** | **str** | The type of Date Regularity | 

## Example

```python
from lusid_workflow.models.year_regularity import YearRegularity

# TODO update the JSON string below
json = "{}"
# create an instance of YearRegularity from a JSON string
year_regularity_instance = YearRegularity.from_json(json)
# print the JSON string representation of the object
print YearRegularity.to_json()

# convert the object into a dict
year_regularity_dict = year_regularity_instance.to_dict()
# create an instance of YearRegularity from a dict
year_regularity_form_dict = year_regularity.from_dict(year_regularity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


