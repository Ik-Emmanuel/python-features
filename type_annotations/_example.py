
from dataclasses import dataclass, field
from typing import Callable, Any, List, Dict, Self, Iterator



# =====================
# validators: list[Callable[[int], bool]] = field(default_factory=list)

# @dataclass
# class Account:
#     ...
# accounts: dict[str, Account] = field(default_factory=dict)
# def __iter__(self) -> Iterator[Account]:




# Callable[[int], bool]: callable use for type annotating functions. This one means takes and integer and returns a boolean

@dataclass
class Validator:
    validators: list[Callable[[int], bool]] = field(default_factory=list)
    

    def add_validator(self, validator: Callable[[int], bool]) -> None:
        self.validators.append(validator)

    # overiding the call dunder method
    def __call__(self, value:int) -> bool:
        return all(validator(value) for validator in self.validators)

ValidatorFn = Callable[[int], bool]

def validate_pipeline(validators: list[ValidatorFn]) -> ValidatorFn:
    def validator(value: int) -> bool:
        return all(validator(value) for validator in validators)

    return validator


# # Define validator functions
# def is_even(value: int) -> bool:
#     return value % 2 == 0


# def is_positive(value: int) -> bool:
#     return value > 0


# def main() -> None:
#     validator = validate_pipeline([is_even, is_positive])

#     # Perform validation
#     result = validator(4)
#     print(result)  # Output: True

#     result = validator(7)
#     print(result)  # Output: False


# if __name__ == "__main__":
#     main()