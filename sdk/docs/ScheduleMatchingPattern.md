# ScheduleMatchingPattern

The Schedule Matching Pattern to trigger on

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ScheduleMatchingPatternContext**](ScheduleMatchingPatternContext.md) |  | 
**recurrence_pattern** | [**RecurrencePattern**](RecurrencePattern.md) |  | 

## Example

```python
from lusid_workflow.models.schedule_matching_pattern import ScheduleMatchingPattern

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleMatchingPattern from a JSON string
schedule_matching_pattern_instance = ScheduleMatchingPattern.from_json(json)
# print the JSON string representation of the object
print ScheduleMatchingPattern.to_json()

# convert the object into a dict
schedule_matching_pattern_dict = schedule_matching_pattern_instance.to_dict()
# create an instance of ScheduleMatchingPattern from a dict
schedule_matching_pattern_form_dict = schedule_matching_pattern.from_dict(schedule_matching_pattern_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


