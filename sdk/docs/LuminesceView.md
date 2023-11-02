# LuminesceView

Configuration for a Worker that calls a Luminesce view

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | 
**name** | **str** | Name of the view in Luminesce | 

## Example

```python
from lusid_workflow.models.luminesce_view import LuminesceView

# TODO update the JSON string below
json = "{}"
# create an instance of LuminesceView from a JSON string
luminesce_view_instance = LuminesceView.from_json(json)
# print the JSON string representation of the object
print LuminesceView.to_json()

# convert the object into a dict
luminesce_view_dict = luminesce_view_instance.to_dict()
# create an instance of LuminesceView from a dict
luminesce_view_form_dict = luminesce_view.from_dict(luminesce_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


