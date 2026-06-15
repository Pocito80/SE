class Sensor:
    def __init__(self, sensorID: str, status: str) -> None:
        self.sensorID: str = sensorID
        self.status: str = status

    def pingStatus(self) -> bool:
        return True

class WaterLevelSensor(Sensor):
    pass
