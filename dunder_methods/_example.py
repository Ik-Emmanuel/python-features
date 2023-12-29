"""
Dunder  or magic methods are used to override or change the behavior of python objects under the hood

use when:
override custom behaviors 
"""

# =====================
# __eq__: a method that is called when validating if 2  objects are same 
# __call__: called when a method is called 
# __new__: a method that is called when an object is created 
# __repr__: used to change the way an object is represented
# __init__: used to initialize a class

# context manager
    # __enter__ : method called when a context manager is called or initiated
    # __exit__: method called when exiting the context manager



from dataclasses import dataclass, field
from typing import Callable



@dataclass
class Validator:
    validators: list[Callable[[int], bool]] = field(default_factory=list)
    def add_validator(self, validator: Callable[[int], bool]) -> None:
        self.validators.append(validator)

    # alter the call method
    def __call__(self, value: int) -> bool:
        return all(validator(value) for validator in self.validators)

# Define validator functions
def is_even(value: int) -> bool:
    return value % 2 == 0
def is_positive(value: int) -> bool:
    return value > 0

# def main() -> None:
#     # Create a Validator instance with multiple validators
#     validator = Validator(validators=[is_even, is_positive])
#     # Perform validation
#     result = validator(4)
#     print(result)  # Output: True
#     result = validator(7)
#     print(result)  # Output: False


# if __name__ == "__main__":
#     main()

# =====================
# __new__: a method that is called when an object is created 

class Payment:
    def __new__(cls, payment_type: str):
        if payment_type == "paypal":
            return object.__new__(PaypalPayment)
        elif payment_type == "card":
            return object.__new__(StripePayment)

    def pay(self, amount: int) -> None:
        raise NotImplementedError
    

class PaypalPayment(Payment):
    def pay(self, amount: int) -> None:
        print(f"Paying ${amount/100:.2f} using Paypal")


class StripePayment(Payment):
    def pay(self, amount: int) -> None:
        print(f"Paying ${amount/100:.2f} using Stripe")

        
def main() -> None:
    my_payment = Payment("card")
    my_payment.pay(100)


if __name__ == "__main__":
    main()


# =====================
# __eq__: a method that is called when validating if 2  objects are same 

from typing import Self

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y
    

def main() -> None:
    # Create a large collection of Point objects
    points = [Point(x, x) for x in range(100000)]

    # Check if a specific point exists in the collection
    target_point = Point(500, 500)

    execution_time = timeit.timeit(lambda: target_point in points, number=10000)
    print(f"Execution time: {execution_time} seconds")


# ========================
# init and repr
    
class Point2:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point2({self.x}, {self.y})"
    


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Self) -> Self:
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    

def main() -> None:
    a = Vector(1, 2)
    b = Vector(3, 4)
    d = Vector(1, 2)
    c = a + b
    print(c)  # Output: Vector(4, 6)
    print(a == b)  # Output: False
    print(a == d)  # Output: True




# ================== context manager
class DatabaseConnection:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.connection = None

    def __enter__(self):
        self.connection = connect(self.host, self.username, self.password)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def main() -> None:
    with DatabaseConnection("localhost", "myuser", "mypassword") as db:
        # Perform database operations
        db.query("SELECT * FROM users")
        # Connection is automatically closed at the end of the 'with' block


