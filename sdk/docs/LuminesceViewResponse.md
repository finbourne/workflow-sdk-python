# LuminesceViewResponse

Readonly configuration for a Worker that calls a Luminesce view

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | [optional] 
**name** | **str** | Name of the view in Luminesce | [optional] 

## Example

```python
from lusid_workflow.models.luminesce_view_response import LuminesceViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LuminesceViewResponse from a JSON string
luminesce_view_response_instance = LuminesceViewResponse.from_json(json)
# print the JSON string representation of the object
print LuminesceViewResponse.to_json()

# convert the object into a dict
luminesce_view_response_dict = luminesce_view_response_instance.to_dict()
# create an instance of LuminesceViewResponse from a dict
luminesce_view_response_form_dict = luminesce_view_response.from_dict(luminesce_view_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


