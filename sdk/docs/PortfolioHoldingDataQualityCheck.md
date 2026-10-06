# PortfolioHoldingDataQualityCheck

Configuration for a Worker that runs a portfolio holding Data quality check in LUSID
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | 
## Example

```python
from lusid_workflow.models.portfolio_holding_data_quality_check import PortfolioHoldingDataQualityCheck
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
portfolio_holding_data_quality_check_instance = PortfolioHoldingDataQualityCheck(type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

