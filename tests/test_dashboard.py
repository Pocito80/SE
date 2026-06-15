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

    def test_check_threshold(self):
        from src.dashboard import Dashboard, ThresholdStatus
        from src.config import ThresholdConfig
        config = ThresholdConfig(warningLevel=10.0, criticalLevel=20.0)
        dashboard = Dashboard(sensors=[], config=config)
        self.assertEqual(dashboard.checkThreshold(5.0), ThresholdStatus.OK)
        self.assertEqual(dashboard.checkThreshold(15.0), ThresholdStatus.WARNING)
        self.assertEqual(dashboard.checkThreshold(25.0), ThresholdStatus.CRITICAL)

    def test_trigger_visual_alert_on_critical(self):
        from unittest.mock import patch
        from src.dashboard import Dashboard
        from src.config import ThresholdConfig
        
        with patch('src.dashboard.AlertManager') as mock_alert_manager_cls:
            mock_alert_manager = mock_alert_manager_cls.return_value
            config = ThresholdConfig(warningLevel=10.0, criticalLevel=20.0)
            
            dashboard = Dashboard(sensors=[], config=config)
            dashboard.updateChart(25.0)
            
            mock_alert_manager.triggerVisualAlert.assert_called_once_with(25.0)

if __name__ == "__main__":
    unittest.main()
