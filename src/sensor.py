class Sensor:
    def __init__(self, sensorID: str, status: str) -> None:
        self.sensorID: str = sensorID
        self.status: str = status

    def pingStatus(self) -> bool:
        return True

class WaterLevelSensor(Sensor):
    def __init__(self, sensorID: str, status: str, initialLevel: float = 0.0) -> None:
        super().__init__(sensorID, status)
        self.currentLevel: float = initialLevel

    def getWaterLevel(self) -> float:
        return self.currentLevel

    def transmitData(self) -> None:
        self.currentLevel += 1.0

