from enum import Enum

class BillboardStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    MAINTENANCE = "maintenance"
