# CutLabelReference

A reference to a Cut Label in LUSID

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of the Cut Label | 
**type** | **str** | The type of Time of Day | 

## Example

```python
from lusid_workflow.models.cut_label_reference import CutLabelReference

# TODO update the JSON string below
json = "{}"
# create an instance of CutLabelReference from a JSON string
cut_label_reference_instance = CutLabelReference.from_json(json)
# print the JSON string representation of the object
print CutLabelReference.to_json()

# convert the object into a dict
cut_label_reference_dict = cut_label_reference_instance.to_dict()
# create an instance of CutLabelReference from a dict
cut_label_reference_form_dict = cut_label_reference.from_dict(cut_label_reference_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


