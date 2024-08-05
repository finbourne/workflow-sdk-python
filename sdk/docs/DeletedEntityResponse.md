# DeletedEntityResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The Uri related to this Entity | [optional] 
**effective_from** | **datetime** | The EffectiveFrom for this response | [optional] 
**as_at** | **datetime** | The AsAt for this response | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid_workflow.models.deleted_entity_response import DeletedEntityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedEntityResponse from a JSON string
deleted_entity_response_instance = DeletedEntityResponse.from_json(json)
# print the JSON string representation of the object
print DeletedEntityResponse.to_json()

# convert the object into a dict
deleted_entity_response_dict = deleted_entity_response_instance.to_dict()
# create an instance of DeletedEntityResponse from a dict
deleted_entity_response_form_dict = deleted_entity_response.from_dict(deleted_entity_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


