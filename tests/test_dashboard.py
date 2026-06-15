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

    def test_update_chart(self):
        from src.dashboard import Dashboard
        dashboard = Dashboard(sensors=[])
        dashboard.updateChart(15.546)
        self.assertEqual(dashboard.displayStatus, 15.55)


if __name__ == "__main__":
    unittest.main()
