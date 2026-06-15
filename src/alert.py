def send_email_api(operatorID: str, message: str) -> None:
    pass

class AlertManager:
    def triggerVisualAlert(self, level: float) -> None:
        pass

    def dispatchEmail(self, operatorID: str) -> None:
        send_email_api(operatorID=operatorID, message="Critical water level alert!")
