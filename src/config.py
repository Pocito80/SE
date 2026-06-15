class ThresholdConfig:
    def __init__(self, warningLevel: float, criticalLevel: float) -> None:
        self.warningLevel: float = warningLevel
        self.criticalLevel: float = criticalLevel
