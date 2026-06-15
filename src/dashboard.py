from typing import List, Optional
from src.sensor import WaterLevelSensor
from src.config import ThresholdConfig

class Dashboard:
    def __init__(self, sensors: List[WaterLevelSensor], config: Optional[ThresholdConfig] = None) -> None:
        self.sensors: List[WaterLevelSensor] = sensors
        self.config: Optional[ThresholdConfig] = config
        self.displayStatus: float = 0.0

    def updateChart(self, level: float) -> None:
        self.displayStatus = round(level, 2)

    def checkThreshold(self, level: float) -> str:
        if self.config is None:
            return "OK"
        if level >= self.config.criticalLevel:
            return "CRITICAL"
        elif level >= self.config.warningLevel:
            return "WARNING"
        return "OK"
