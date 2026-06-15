from enum import Enum
from typing import List, Optional
from src.sensor import WaterLevelSensor
from src.config import ThresholdConfig

class ThresholdStatus(Enum):
    OK = "OK"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"

class Dashboard:
    def __init__(self, sensors: List[WaterLevelSensor], config: Optional[ThresholdConfig] = None) -> None:
        self.sensors: List[WaterLevelSensor] = sensors
        self.config: Optional[ThresholdConfig] = config
        self.displayStatus: float = 0.0

    def updateChart(self, level: float) -> None:
        self.displayStatus = round(level, 2)

    def checkThreshold(self, level: float) -> ThresholdStatus:
        if self.config is None:
            return ThresholdStatus.OK
        if level >= self.config.criticalLevel:
            return ThresholdStatus.CRITICAL
        elif level >= self.config.warningLevel:
            return ThresholdStatus.WARNING
        return ThresholdStatus.OK
