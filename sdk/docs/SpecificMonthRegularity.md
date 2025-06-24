# SpecificMonthRegularity

Specific Month Regularity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | The frequency of the Specific Month Regularity | 
**days_of_month** | **List[int]** | Days of the month | 
**type** | **str** | The type of Date Regularity | 

## Example

```python
from lusid_workflow.models.specific_month_regularity import SpecificMonthRegularity

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificMonthRegularity from a JSON string
specific_month_regularity_instance = SpecificMonthRegularity.from_json(json)
# print the JSON string representation of the object
print SpecificMonthRegularity.to_json()

# convert the object into a dict
specific_month_regularity_dict = specific_month_regularity_instance.to_dict()
# create an instance of SpecificMonthRegularity from a dict
specific_month_regularity_form_dict = specific_month_regularity.from_dict(specific_month_regularity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


