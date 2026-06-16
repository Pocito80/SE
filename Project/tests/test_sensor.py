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

    def test_get_water_level(self):
        from src.sensor import WaterLevelSensor
        sensor = WaterLevelSensor(sensorID="sensor-123", status="OK", initialLevel=12.34)
        self.assertEqual(sensor.getWaterLevel(), 12.34)

    def test_transmit_data(self):
        from src.sensor import WaterLevelSensor
        sensor = WaterLevelSensor(sensorID="sensor-123", status="OK", initialLevel=5.0)
        sensor.transmitData()
        self.assertNotEqual(sensor.getWaterLevel(), 5.0)
        
        sensor.transmitData(forcedValue=15.7)
        self.assertEqual(sensor.getWaterLevel(), 15.7)

if __name__ == "__main__":
    unittest.main()
