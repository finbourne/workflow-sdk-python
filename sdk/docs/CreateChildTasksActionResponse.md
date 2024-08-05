# CreateChildTasksActionResponse

Defines a read-only Create Child Tasks Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | [optional] 
**child_task_configurations** | [**List[CreateChildTaskConfiguration]**](CreateChildTaskConfiguration.md) | The Child Task Configurations | [optional] 

## Example

```python
from lusid_workflow.models.create_child_tasks_action_response import CreateChildTasksActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChildTasksActionResponse from a JSON string
create_child_tasks_action_response_instance = CreateChildTasksActionResponse.from_json(json)
# print the JSON string representation of the object
print CreateChildTasksActionResponse.to_json()

# convert the object into a dict
create_child_tasks_action_response_dict = create_child_tasks_action_response_instance.to_dict()
# create an instance of CreateChildTasksActionResponse from a dict
create_child_tasks_action_response_form_dict = create_child_tasks_action_response.from_dict(create_child_tasks_action_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


