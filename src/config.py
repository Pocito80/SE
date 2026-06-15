class ThresholdConfig:
    def __init__(self, warningLevel: float, criticalLevel: float) -> None:
        self.warningLevel: float = warningLevel
        self.criticalLevel: float = criticalLevel

    def updateThresholds(self, warningLevel, criticalLevel):
        self.warningLevel = warningLevel
        self.criticalLevel = criticalLevel
