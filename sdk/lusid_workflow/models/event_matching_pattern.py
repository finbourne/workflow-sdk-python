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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator

class EventMatchingPattern(BaseModel):
    """
    The matching event pattern object  # noqa: E501
    """
    event_type: constr(strict=True, max_length=512, min_length=0) = Field(..., alias="eventType", description="The type of event to subscribe to. The list of available event types can be discovered  by calling the ‘List available EventTypes’ API endpoint in the Notifications service")
    filter: Optional[StrictStr] = Field(None, description="A filter on the event. See https://support.lusid.com/filtering-results-from-lusid for more information.  If not provided, all events will be matched.")
    __properties = ["eventType", "filter"]

    @validator('event_type')
    def event_type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z]*$/")
        return value

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
    def from_json(cls, json_str: str) -> EventMatchingPattern:
        """Create an instance of EventMatchingPattern from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if filter (nullable) is None
        # and __fields_set__ contains the field
        if self.filter is None and "filter" in self.__fields_set__:
            _dict['filter'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventMatchingPattern:
        """Create an instance of EventMatchingPattern from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventMatchingPattern.parse_obj(obj)

        _obj = EventMatchingPattern.parse_obj({
            "event_type": obj.get("eventType"),
            "filter": obj.get("filter")
        })
        return _obj
