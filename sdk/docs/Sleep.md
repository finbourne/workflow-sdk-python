# Sleep

Configuration for a Worker that Sleeps for a user-defined amount of time

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | 

## Example

```python
from lusid_workflow.models.sleep import Sleep

# TODO update the JSON string below
json = "{}"
# create an instance of Sleep from a JSON string
sleep_instance = Sleep.from_json(json)
# print the JSON string representation of the object
print Sleep.to_json()

# convert the object into a dict
sleep_dict = sleep_instance.to_dict()
# create an instance of Sleep from a dict
sleep_form_dict = sleep.from_dict(sleep_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


