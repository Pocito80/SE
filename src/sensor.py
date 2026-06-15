class Sensor:
    def __init__(self, sensorID: str, status: str) -> None:
        self.sensorID: str = sensorID
        self.status: str = status

class WaterLevelSensor(Sensor):
    pass
