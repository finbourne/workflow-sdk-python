# TimeConstraints

Time constraints for a Recurrence Pattern

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Start date of the Recurrence Pattern | 
**end_date** | **str** | Optional end date of the Recurrence Pattern | [optional] 
**times_of_day** | [**List[TimeOfDay]**](TimeOfDay.md) | Times of the day to run the Recurrence Pattern | 

## Example

```python
from lusid_workflow.models.time_constraints import TimeConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of TimeConstraints from a JSON string
time_constraints_instance = TimeConstraints.from_json(json)
# print the JSON string representation of the object
print TimeConstraints.to_json()

# convert the object into a dict
time_constraints_dict = time_constraints_instance.to_dict()
# create an instance of TimeConstraints from a dict
time_constraints_form_dict = time_constraints.from_dict(time_constraints_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


