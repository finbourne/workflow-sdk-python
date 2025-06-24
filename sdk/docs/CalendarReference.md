# CalendarReference

Reference to a Calendar in LUSID

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the Calendar | 
**code** | **str** | The code of the Calendar | 

## Example

```python
from lusid_workflow.models.calendar_reference import CalendarReference

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarReference from a JSON string
calendar_reference_instance = CalendarReference.from_json(json)
# print the JSON string representation of the object
print CalendarReference.to_json()

# convert the object into a dict
calendar_reference_dict = calendar_reference_instance.to_dict()
# create an instance of CalendarReference from a dict
calendar_reference_form_dict = calendar_reference.from_dict(calendar_reference_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


