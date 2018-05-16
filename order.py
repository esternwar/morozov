from datetime import datetime


class Order:
    id = 0
    weight = 0
    size = 0
    loginCostumer = ""
    loginExecutor = ""
    price = 0
    status = ""
    addressPickup = ""
    addressDelivery = ""
    timePickup = datetime.now()
    timeDelivery = datetime.now()
    description = ""
    rejectionReason = ""
