# CreateChildTasksAction

Defines a Create Child Tasks Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | 
**child_task_configurations** | [**List[CreateChildTaskConfiguration]**](CreateChildTaskConfiguration.md) | The Child Task Configurations | 

## Example

```python
from lusid_workflow.models.create_child_tasks_action import CreateChildTasksAction

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChildTasksAction from a JSON string
create_child_tasks_action_instance = CreateChildTasksAction.from_json(json)
# print the JSON string representation of the object
print CreateChildTasksAction.to_json()

# convert the object into a dict
create_child_tasks_action_dict = create_child_tasks_action_instance.to_dict()
# create an instance of CreateChildTasksAction from a dict
create_child_tasks_action_form_dict = create_child_tasks_action.from_dict(create_child_tasks_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


