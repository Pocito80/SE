class ThresholdConfig:
    def __init__(self, warningLevel: float, criticalLevel: float) -> None:
        if warningLevel >= criticalLevel:
            raise ValueError("warningLevel must be less than criticalLevel")
        self.warningLevel: float = warningLevel
        self.criticalLevel: float = criticalLevel

    def updateThresholds(self, warningLevel: float, criticalLevel: float) -> None:
        if warningLevel >= criticalLevel:
            raise ValueError("warningLevel must be less than criticalLevel")
        self.warningLevel = warningLevel
        self.criticalLevel = criticalLevel
