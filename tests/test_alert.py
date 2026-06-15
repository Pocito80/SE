import unittest
from unittest.mock import patch

class TestAlertManagerEmail(unittest.TestCase):
    def test_dispatch_email_calls_external_api(self):
        with patch('src.alert.send_email_api') as mock_send_email:
            from src.alert import AlertManager
            manager = AlertManager()
            
            operator_id = "op-456"
            manager.dispatchEmail(operator_id)
            
            mock_send_email.assert_called_once_with(operatorID=operator_id, message="Critical water level alert!")

if __name__ == "__main__":
    unittest.main()
