from typing import Dict, Any
from pydantic import BaseModel

class ThresholdEvent(BaseModel):
    rule_name: str
    metric: str
    current_value: float
    baseline_value: float
    threshold_type: str
    threshold_value: float
    time_window: str
    supporting_metrics: Dict[str, Dict[str, Any]]
