# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, conlist, constr 
from lusid_workflow.models.action_definition import ActionDefinition
from lusid_workflow.models.initial_state import InitialState
from lusid_workflow.models.resource_id import ResourceId
from lusid_workflow.models.task_field_definition import TaskFieldDefinition
from lusid_workflow.models.task_state_definition import TaskStateDefinition
from lusid_workflow.models.task_transition_definition import TaskTransitionDefinition
from lusid_workflow.models.transition_trigger_definition import TransitionTriggerDefinition

class CreateTaskDefinitionRequest(BaseModel):
    """
    Contains required info to create a new Task Definition  # noqa: E501
    """
    id: ResourceId = Field(...)
    display_name:  StrictStr = Field(...,alias="displayName", description="Human readable name") 
    description:  Optional[StrictStr] = Field(None,alias="description", description="Human readable description") 
    states: conlist(TaskStateDefinition, min_items=1) = Field(..., description="The states this Task Definition operates over")
    field_schema: Optional[conlist(TaskFieldDefinition)] = Field(None, alias="fieldSchema", description="Defines the fields associated with this Task")
    initial_state: InitialState = Field(..., alias="initialState")
    triggers: Optional[conlist(TransitionTriggerDefinition)] = Field(None, description="Triggers")
    transitions: Optional[conlist(TaskTransitionDefinition)] = Field(None, description="Transitions")
    actions: Optional[conlist(ActionDefinition)] = Field(None, description="Actions")
    __properties = ["id", "displayName", "description", "states", "fieldSchema", "initialState", "triggers", "transitions", "actions"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CreateTaskDefinitionRequest:
        """Create an instance of CreateTaskDefinitionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in states (list)
        _items = []
        if self.states:
            for _item in self.states:
                if _item:
                    _items.append(_item.to_dict())
            _dict['states'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in field_schema (list)
        _items = []
        if self.field_schema:
            for _item in self.field_schema:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fieldSchema'] = _items
        # override the default output from pydantic by calling `to_dict()` of initial_state
        if self.initial_state:
            _dict['initialState'] = self.initial_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in triggers (list)
        _items = []
        if self.triggers:
            for _item in self.triggers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['triggers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in transitions (list)
        _items = []
        if self.transitions:
            for _item in self.transitions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transitions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item in self.actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['actions'] = _items
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if field_schema (nullable) is None
        # and __fields_set__ contains the field
        if self.field_schema is None and "field_schema" in self.__fields_set__:
            _dict['fieldSchema'] = None

        # set to None if triggers (nullable) is None
        # and __fields_set__ contains the field
        if self.triggers is None and "triggers" in self.__fields_set__:
            _dict['triggers'] = None

        # set to None if transitions (nullable) is None
        # and __fields_set__ contains the field
        if self.transitions is None and "transitions" in self.__fields_set__:
            _dict['transitions'] = None

        # set to None if actions (nullable) is None
        # and __fields_set__ contains the field
        if self.actions is None and "actions" in self.__fields_set__:
            _dict['actions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateTaskDefinitionRequest:
        """Create an instance of CreateTaskDefinitionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateTaskDefinitionRequest.parse_obj(obj)

        _obj = CreateTaskDefinitionRequest.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "states": [TaskStateDefinition.from_dict(_item) for _item in obj.get("states")] if obj.get("states") is not None else None,
            "field_schema": [TaskFieldDefinition.from_dict(_item) for _item in obj.get("fieldSchema")] if obj.get("fieldSchema") is not None else None,
            "initial_state": InitialState.from_dict(obj.get("initialState")) if obj.get("initialState") is not None else None,
            "triggers": [TransitionTriggerDefinition.from_dict(_item) for _item in obj.get("triggers")] if obj.get("triggers") is not None else None,
            "transitions": [TaskTransitionDefinition.from_dict(_item) for _item in obj.get("transitions")] if obj.get("transitions") is not None else None,
            "actions": [ActionDefinition.from_dict(_item) for _item in obj.get("actions")] if obj.get("actions") is not None else None
        })
        return _obj
