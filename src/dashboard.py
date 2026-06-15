from typing import List
from src.sensor import WaterLevelSensor

class Dashboard:
    def __init__(self, sensors: List[WaterLevelSensor]) -> None:
        self.sensors: List[WaterLevelSensor] = sensors
        self.displayStatus: float = 0.0

    def updateChart(self, level: float) -> None:
        self.displayStatus = level
