# VersionInfo

The version metadata.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_created** | **datetime** | The asAt datetime at which this entity was first created. | [optional] 
**user_id_created** | **str** | The unique id of the user who created this entity. | [optional] 
**request_id_created** | **str** | The request id of the request that created this entity. | [optional] 
**as_at_modified** | **datetime** | The asAt datetime at which this entity was last updated. | [optional] 
**user_id_modified** | **str** | The unique id of the user who last updated this entity. | [optional] 
**request_id_modified** | **str** | The request id of the request that last updated this entity. | [optional] 
**as_at_version_number** | **int** | The integer version number for this entity (the entity was created at version 1). | [optional] 

## Example

```python
from lusid_workflow.models.version_info import VersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VersionInfo from a JSON string
version_info_instance = VersionInfo.from_json(json)
# print the JSON string representation of the object
print VersionInfo.to_json()

# convert the object into a dict
version_info_dict = version_info_instance.to_dict()
# create an instance of VersionInfo from a dict
version_info_form_dict = version_info.from_dict(version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


