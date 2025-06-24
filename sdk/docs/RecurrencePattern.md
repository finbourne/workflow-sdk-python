# RecurrencePattern

The Recurrence Pattern

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_constraints** | [**TimeConstraints**](TimeConstraints.md) |  | 
**date_regularity** | [**DateRegularity**](DateRegularity.md) |  | 
**business_day_adjustment** | **str** | The Business Day Adjustment | 

## Example

```python
from lusid_workflow.models.recurrence_pattern import RecurrencePattern

# TODO update the JSON string below
json = "{}"
# create an instance of RecurrencePattern from a JSON string
recurrence_pattern_instance = RecurrencePattern.from_json(json)
# print the JSON string representation of the object
print RecurrencePattern.to_json()

# convert the object into a dict
recurrence_pattern_dict = recurrence_pattern_instance.to_dict()
# create an instance of RecurrencePattern from a dict
recurrence_pattern_form_dict = recurrence_pattern.from_dict(recurrence_pattern_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


