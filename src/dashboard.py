from typing import List
from src.sensor import WaterLevelSensor

class Dashboard:
    def __init__(self, sensors: List[WaterLevelSensor]) -> None:
        self.sensors: List[WaterLevelSensor] = sensors
