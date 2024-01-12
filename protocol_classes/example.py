from typing import Protocol

class ShapeProtocol(Protocol):
    def area(self) -> float:
        ...

    def perimeter(self) -> float:
        ...
        
from dataclasses import dataclass

@dataclass
class Card:
    number: str
    exp_month: int
    exp_year: int
    valid: bool = False


class CardInfo(Protocol):
    @property
    def number(self) -> str:
        ...

    @property
    def exp_month(self) -> int:
        ...

    @property
    def exp_year(self) -> int:
        ...


def validate_card(card: CardInfo) -> bool:
    return (
        True
    )