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
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator
from lusid_workflow.models.fail_response import FailResponse
from lusid_workflow.models.group_reconciliation_response import GroupReconciliationResponse
from lusid_workflow.models.health_check_response import HealthCheckResponse
from lusid_workflow.models.luminesce_view_response import LuminesceViewResponse
from lusid_workflow.models.scheduler_job_response import SchedulerJobResponse
from lusid_workflow.models.sleep_response import SleepResponse
from typing import Union, Any, List, TYPE_CHECKING
from pydantic.v1 import StrictStr, Field

WORKERCONFIGURATIONRESPONSE_ONE_OF_SCHEMAS = ["FailResponse", "GroupReconciliationResponse", "HealthCheckResponse", "LuminesceViewResponse", "SchedulerJobResponse", "SleepResponse"]

class WorkerConfigurationResponse(BaseModel):
    """
    Readonly information about how the worker should be executed
    """
    # data type: FailResponse
    oneof_schema_1_validator: Optional[FailResponse] = None
    # data type: GroupReconciliationResponse
    oneof_schema_2_validator: Optional[GroupReconciliationResponse] = None
    # data type: HealthCheckResponse
    oneof_schema_3_validator: Optional[HealthCheckResponse] = None
    # data type: LuminesceViewResponse
    oneof_schema_4_validator: Optional[LuminesceViewResponse] = None
    # data type: SchedulerJobResponse
    oneof_schema_5_validator: Optional[SchedulerJobResponse] = None
    # data type: SleepResponse
    oneof_schema_6_validator: Optional[SleepResponse] = None
    if TYPE_CHECKING:
        actual_instance: Union[FailResponse, GroupReconciliationResponse, HealthCheckResponse, LuminesceViewResponse, SchedulerJobResponse, SleepResponse]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(WORKERCONFIGURATIONRESPONSE_ONE_OF_SCHEMAS, const=True)

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
        instance = WorkerConfigurationResponse.construct()
        error_messages = []
        match = 0
        # validate data type: FailResponse
        if not isinstance(v, FailResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FailResponse`")
        else:
            match += 1
        # validate data type: GroupReconciliationResponse
        if not isinstance(v, GroupReconciliationResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GroupReconciliationResponse`")
        else:
            match += 1
        # validate data type: HealthCheckResponse
        if not isinstance(v, HealthCheckResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HealthCheckResponse`")
        else:
            match += 1
        # validate data type: LuminesceViewResponse
        if not isinstance(v, LuminesceViewResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LuminesceViewResponse`")
        else:
            match += 1
        # validate data type: SchedulerJobResponse
        if not isinstance(v, SchedulerJobResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SchedulerJobResponse`")
        else:
            match += 1
        # validate data type: SleepResponse
        if not isinstance(v, SleepResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SleepResponse`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in WorkerConfigurationResponse with oneOf schemas: FailResponse, GroupReconciliationResponse, HealthCheckResponse, LuminesceViewResponse, SchedulerJobResponse, SleepResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in WorkerConfigurationResponse with oneOf schemas: FailResponse, GroupReconciliationResponse, HealthCheckResponse, LuminesceViewResponse, SchedulerJobResponse, SleepResponse. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> WorkerConfigurationResponse:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> WorkerConfigurationResponse:
        """Returns the object represented by the json string"""
        instance = WorkerConfigurationResponse.construct()
        error_messages = []
        match = 0

        # deserialize data into FailResponse
        try:
            instance.actual_instance = FailResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GroupReconciliationResponse
        try:
            instance.actual_instance = GroupReconciliationResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HealthCheckResponse
        try:
            instance.actual_instance = HealthCheckResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LuminesceViewResponse
        try:
            instance.actual_instance = LuminesceViewResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SchedulerJobResponse
        try:
            instance.actual_instance = SchedulerJobResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SleepResponse
        try:
            instance.actual_instance = SleepResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into WorkerConfigurationResponse with oneOf schemas: FailResponse, GroupReconciliationResponse, HealthCheckResponse, LuminesceViewResponse, SchedulerJobResponse, SleepResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into WorkerConfigurationResponse with oneOf schemas: FailResponse, GroupReconciliationResponse, HealthCheckResponse, LuminesceViewResponse, SchedulerJobResponse, SleepResponse. Details: " + ", ".join(error_messages))
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
