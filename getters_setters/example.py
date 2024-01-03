
from dataclasses import dataclass, field    


@dataclass 
class Order:
    items: list[LineItem] = field(default_ factory=list)
    _payment_status: PaymentStatus = PaymentStatus.PENDING

    def add_item(self, item: LineItem) :
        self.items.append(item)
        
    # getter
    def get_payment_status(self) -> PaymentStatus:
        return self ._payment_status
    
    # setter
    def set_payment_status (self, status: PaymentStatus) -> None:
    # here, using a (getter +) setter is okay, because we're doing something
    # more than just setting the value
        if self._payment_status == PaymentStatus. PAID:
            raise PaymentStatusError(
            "You can't change the status of an already paid order."
            )
        self._payment_status = status

    @property
    def total_price(self) -> int:
        return sum(item. total_price for item in self.items)