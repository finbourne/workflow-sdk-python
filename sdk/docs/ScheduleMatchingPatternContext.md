# ScheduleMatchingPatternContext

Context for a Schedule Matching Pattern

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zone** | **str** | The time zone to use | 
**holiday_calendars** | [**List[CalendarReference]**](CalendarReference.md) | References to any Holiday Calendars to use | [optional] 

## Example

```python
from lusid_workflow.models.schedule_matching_pattern_context import ScheduleMatchingPatternContext

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleMatchingPatternContext from a JSON string
schedule_matching_pattern_context_instance = ScheduleMatchingPatternContext.from_json(json)
# print the JSON string representation of the object
print ScheduleMatchingPatternContext.to_json()

# convert the object into a dict
schedule_matching_pattern_context_dict = schedule_matching_pattern_context_instance.to_dict()
# create an instance of ScheduleMatchingPatternContext from a dict
schedule_matching_pattern_context_form_dict = schedule_matching_pattern_context.from_dict(schedule_matching_pattern_context_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


