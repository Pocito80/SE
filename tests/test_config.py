import unittest

class TestThresholdConfig(unittest.TestCase):
    def test_threshold_config_initialization(self):
        from src.config import ThresholdConfig
        config = ThresholdConfig(warningLevel=10.0, criticalLevel=20.0)
        self.assertEqual(config.warningLevel, 10.0)
        self.assertEqual(config.criticalLevel, 20.0)

if __name__ == "__main__":
    unittest.main()
