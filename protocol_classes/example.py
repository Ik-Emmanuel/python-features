from typing import Protocol

class ShapeProtocol(Protocol):
    def area(self) -> float:
        ...

    def perimeter(self) -> float:
        ...