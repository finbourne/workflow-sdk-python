# RelativeMonthRegularity

Relative Month Regularity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | The frequency of the Relative Month Regularity | 
**days_of_week** | **List[str]** | Days of the week | 
**index** | **str** | Relative index in the month | 
**type** | **str** | The type of Date Regularity | 

## Example

```python
from lusid_workflow.models.relative_month_regularity import RelativeMonthRegularity

# TODO update the JSON string below
json = "{}"
# create an instance of RelativeMonthRegularity from a JSON string
relative_month_regularity_instance = RelativeMonthRegularity.from_json(json)
# print the JSON string representation of the object
print RelativeMonthRegularity.to_json()

# convert the object into a dict
relative_month_regularity_dict = relative_month_regularity_instance.to_dict()
# create an instance of RelativeMonthRegularity from a dict
relative_month_regularity_form_dict = relative_month_regularity.from_dict(relative_month_regularity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


