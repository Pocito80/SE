import unittest
from unittest.mock import patch

class TestAlertManagerEmail(unittest.TestCase):
    def test_dispatch_email_calls_external_api(self):
        # We will mock the external email API function send_email_api inside src.alert module
        with patch('src.alert.send_email_api') as mock_send_email:
            from src.alert import AlertManager, EMAIL_ALERT_TEMPLATE
            manager = AlertManager()
            
            operator_id = "op-456"
            manager.dispatchEmail(operator_id)
            
            # Assert exactly one call with correct parameters
            mock_send_email.assert_called_once_with(operatorID=operator_id, message=EMAIL_ALERT_TEMPLATE)

if __name__ == "__main__":
    unittest.main()
