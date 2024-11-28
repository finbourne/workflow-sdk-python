# GroupReconciliation

Configuration for a Worker that calls runs a Group Reconciliation in LUSID

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | 

## Example

```python
from lusid_workflow.models.group_reconciliation import GroupReconciliation

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliation from a JSON string
group_reconciliation_instance = GroupReconciliation.from_json(json)
# print the JSON string representation of the object
print GroupReconciliation.to_json()

# convert the object into a dict
group_reconciliation_dict = group_reconciliation_instance.to_dict()
# create an instance of GroupReconciliation from a dict
group_reconciliation_form_dict = group_reconciliation.from_dict(group_reconciliation_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


