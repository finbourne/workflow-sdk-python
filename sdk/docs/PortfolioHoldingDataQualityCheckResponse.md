# PortfolioHoldingDataQualityCheckResponse

Readonly configuration for the Portfolio Holding Data Quality Check Worker
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | [optional] 
## Example

```python
from lusid_workflow.models.portfolio_holding_data_quality_check_response import PortfolioHoldingDataQualityCheckResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
portfolio_holding_data_quality_check_response_instance = PortfolioHoldingDataQualityCheckResponse(type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

