import enum

class DataQualityEnum(enum.Enum):
    EXCELLENT = "excellent"  # 0.95–1.0
    GOOD = "good"            # 0.85–0.94
    FAIR = "fair"            # 0.70–0.84
    POOR = "poor"            # < 0.70