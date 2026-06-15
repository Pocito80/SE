import unittest

class TestDashboard(unittest.TestCase):
    def test_dashboard_sensor_aggregation(self):
        from src.sensor import WaterLevelSensor
        from src.dashboard import Dashboard

        sensor1 = WaterLevelSensor(sensorID="sensor-1", status="OK")
        sensor2 = WaterLevelSensor(sensorID="sensor-2", status="OK")
        sensors = [sensor1, sensor2]

        dashboard = Dashboard(sensors=sensors)
        self.assertEqual(dashboard.sensors, sensors)

if __name__ == "__main__":
    unittest.main()
