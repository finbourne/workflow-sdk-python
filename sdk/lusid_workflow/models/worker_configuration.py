# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from lusid_workflow.models.fail import Fail
from lusid_workflow.models.health_check import HealthCheck
from lusid_workflow.models.luminesce_view import LuminesceView
from lusid_workflow.models.sleep import Sleep
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

WORKERCONFIGURATION_ONE_OF_SCHEMAS = ["Fail", "HealthCheck", "LuminesceView", "Sleep"]

class WorkerConfiguration(BaseModel):
    """
    Information about how the worker should be executed
    """
    # data type: Fail
    oneof_schema_1_validator: Optional[Fail] = None
    # data type: HealthCheck
    oneof_schema_2_validator: Optional[HealthCheck] = None
    # data type: LuminesceView
    oneof_schema_3_validator: Optional[LuminesceView] = None
    # data type: Sleep
    oneof_schema_4_validator: Optional[Sleep] = None
    if TYPE_CHECKING:
        actual_instance: Union[Fail, HealthCheck, LuminesceView, Sleep]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(WORKERCONFIGURATION_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = WorkerConfiguration.construct()
        error_messages = []
        match = 0
        # validate data type: Fail
        if not isinstance(v, Fail):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Fail`")
        else:
            match += 1
        # validate data type: HealthCheck
        if not isinstance(v, HealthCheck):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HealthCheck`")
        else:
            match += 1
        # validate data type: LuminesceView
        if not isinstance(v, LuminesceView):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LuminesceView`")
        else:
            match += 1
        # validate data type: Sleep
        if not isinstance(v, Sleep):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Sleep`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in WorkerConfiguration with oneOf schemas: Fail, HealthCheck, LuminesceView, Sleep. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in WorkerConfiguration with oneOf schemas: Fail, HealthCheck, LuminesceView, Sleep. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> WorkerConfiguration:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> WorkerConfiguration:
        """Returns the object represented by the json string"""
        instance = WorkerConfiguration.construct()
        error_messages = []
        match = 0

        # deserialize data into Fail
        try:
            instance.actual_instance = Fail.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HealthCheck
        try:
            instance.actual_instance = HealthCheck.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LuminesceView
        try:
            instance.actual_instance = LuminesceView.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Sleep
        try:
            instance.actual_instance = Sleep.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into WorkerConfiguration with oneOf schemas: Fail, HealthCheck, LuminesceView, Sleep. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into WorkerConfiguration with oneOf schemas: Fail, HealthCheck, LuminesceView, Sleep. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())
