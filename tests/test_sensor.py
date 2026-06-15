import unittest

class TestWaterLevelSensor(unittest.TestCase):
    def test_sensor_initialization(self):
        from src.sensor import WaterLevelSensor
        sensor = WaterLevelSensor(sensorID="sensor-123", status="OK")
        self.assertEqual(sensor.sensorID, "sensor-123")
        self.assertEqual(sensor.status, "OK")

    def test_ping_status(self):
        from src.sensor import WaterLevelSensor
        sensor = WaterLevelSensor(sensorID="sensor-123", status="OK")
        self.assertTrue(sensor.pingStatus())

if __name__ == "__main__":
    unittest.main()
