import unittest

class TestThresholdConfig(unittest.TestCase):
    def test_threshold_config_initialization(self):
        from src.config import ThresholdConfig
        config = ThresholdConfig(warningLevel=10.0, criticalLevel=20.0)
        self.assertEqual(config.warningLevel, 10.0)
        self.assertEqual(config.criticalLevel, 20.0)

    def test_update_thresholds(self):
        from src.config import ThresholdConfig
        config = ThresholdConfig(warningLevel=10.0, criticalLevel=20.0)
        config.updateThresholds(12.0, 22.0)
        self.assertEqual(config.warningLevel, 12.0)
        self.assertEqual(config.criticalLevel, 22.0)

    def test_invalid_thresholds(self):
        from src.config import ThresholdConfig
        with self.assertRaises(ValueError):
            ThresholdConfig(warningLevel=20.0, criticalLevel=10.0)
        with self.assertRaises(ValueError):
            ThresholdConfig(warningLevel=15.0, criticalLevel=15.0)

        config = ThresholdConfig(warningLevel=10.0, criticalLevel=20.0)
        with self.assertRaises(ValueError):
            config.updateThresholds(25.0, 20.0)

if __name__ == "__main__":
    unittest.main()
