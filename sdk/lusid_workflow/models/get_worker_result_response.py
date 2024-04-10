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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

class GetWorkerResultResponse(BaseModel):
    """
    The RunWorker response  # noqa: E501
    """
    worker_status: constr(strict=True, min_length=1) = Field(..., alias="workerStatus", description="The final status of the Worker")
    results: conlist(Dict[str, Any]) = Field(..., description="Results")
    status_detail: Optional[StrictStr] = Field(None, alias="statusDetail", description="Detail on the final status")
    __properties = ["workerStatus", "results", "statusDetail"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GetWorkerResultResponse:
        """Create an instance of GetWorkerResultResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if status_detail (nullable) is None
        # and __fields_set__ contains the field
        if self.status_detail is None and "status_detail" in self.__fields_set__:
            _dict['statusDetail'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetWorkerResultResponse:
        """Create an instance of GetWorkerResultResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetWorkerResultResponse.parse_obj(obj)

        _obj = GetWorkerResultResponse.parse_obj({
            "worker_status": obj.get("workerStatus"),
            "results": obj.get("results"),
            "status_detail": obj.get("statusDetail")
        })
        return _obj
