# GroupReconciliationResponse

Readonly configuration for the Group Reconciliation Worker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | [optional] 

## Example

```python
from lusid_workflow.models.group_reconciliation_response import GroupReconciliationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationResponse from a JSON string
group_reconciliation_response_instance = GroupReconciliationResponse.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationResponse.to_json()

# convert the object into a dict
group_reconciliation_response_dict = group_reconciliation_response_instance.to_dict()
# create an instance of GroupReconciliationResponse from a dict
group_reconciliation_response_form_dict = group_reconciliation_response.from_dict(group_reconciliation_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


