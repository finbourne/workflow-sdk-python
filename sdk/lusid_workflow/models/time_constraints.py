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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, conlist, constr 
from lusid_workflow.models.time_of_day import TimeOfDay

class TimeConstraints(BaseModel):
    """
    Time constraints for a Recurrence Pattern  # noqa: E501
    """
    start_date:  StrictStr = Field(...,alias="startDate", description="Start date of the Recurrence Pattern") 
    end_date:  Optional[StrictStr] = Field(None,alias="endDate", description="Optional end date of the Recurrence Pattern") 
    times_of_day: conlist(TimeOfDay) = Field(..., alias="timesOfDay", description="Times of the day to run the Recurrence Pattern")
    __properties = ["startDate", "endDate", "timesOfDay"]

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
    def from_json(cls, json_str: str) -> TimeConstraints:
        """Create an instance of TimeConstraints from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in times_of_day (list)
        _items = []
        if self.times_of_day:
            for _item in self.times_of_day:
                if _item:
                    _items.append(_item.to_dict())
            _dict['timesOfDay'] = _items
        # set to None if end_date (nullable) is None
        # and __fields_set__ contains the field
        if self.end_date is None and "end_date" in self.__fields_set__:
            _dict['endDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TimeConstraints:
        """Create an instance of TimeConstraints from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TimeConstraints.parse_obj(obj)

        _obj = TimeConstraints.parse_obj({
            "start_date": obj.get("startDate"),
            "end_date": obj.get("endDate"),
            "times_of_day": [TimeOfDay.from_dict(_item) for _item in obj.get("timesOfDay")] if obj.get("timesOfDay") is not None else None
        })
        return _obj
