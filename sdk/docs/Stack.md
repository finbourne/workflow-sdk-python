# Stack

Information pertaining to the Tasks Stack if one is present

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_added_as_at** | **datetime** | When the Task was added to the Stack | [optional] 
**stack_opened_as_at** | **datetime** | When the Stack was opened | [optional] 
**stack_closed_as_at** | **datetime** | When the Stack was closed | [optional] 
**stack_membership_type** | **str** | Whether the task is the Lead task of the Stack or a Member within the Stack | [optional] 
**stack_status** | **str** | Status of the Stack (Open/Closed) | [optional] 
**lead_task_id** | **str** | ID of the Lead Task | [optional] 
**lead_task_state** | **str** | State of the Lead Task | [optional] 
**tasks_in_stack** | **int** | Number of Tasks in the Stack | [optional] 

## Example

```python
from lusid_workflow.models.stack import Stack

# TODO update the JSON string below
json = "{}"
# create an instance of Stack from a JSON string
stack_instance = Stack.from_json(json)
# print the JSON string representation of the object
print Stack.to_json()

# convert the object into a dict
stack_dict = stack_instance.to_dict()
# create an instance of Stack from a dict
stack_form_dict = stack.from_dict(stack_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


