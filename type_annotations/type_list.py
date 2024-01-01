"""
Listing all typing types
"""
from typing import List

# 1. String
def greet(name: str) -> str:
    return f"Hello, {name}"


# 2 float 
def calculate_distance(x: float, y: float) -> float:
    return (x**2 + y**2)**0.5


# 3 list of integers or strings 

def process_numbers(numbers: List[int]) -> List[int]:
    return [num * 2 for num in numbers]

def capitalize_words(words: List[str]) -> List[str]:
    return [word.capitalize() for word in words]


# 3b Tuples Tuple[int, int] = (10, 20)  # Tuple
from typing import Tuple

def coordinates(point: Tuple[float, float]) -> str:
    return f"X: {point[0]}, Y: {point[1]}"


# 4 dictionary
# Dict[str, str] = {"name": "Bob", "email": "bob@example.com"} 
from typing import Dict

def process_data(data: Dict[str, int]) -> Dict[str, int]:
    return {key: value * 2 for key, value in data.items()}              




# 5 optional 
from typing import Optional

def greet_optional(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, Guest"
    return f"Hello, {name}"


#6  Union 
from typing import Union

def square_or_double(number: Union[int, float]) -> Union[int, float]:
    if isinstance(number, int):
        return number ** 2
    elif isinstance(number, float):
        return number * 2
    

# 7. Callable 
from typing import Callable

def perform_operation(operation: Callable[[int, int], int], a: int, b: int) -> int:
    return operation(a, b)



# 8 generic types
from typing import TypeVar
T = TypeVar("T")  # Generic type variable

def first_item(items: List[T]) -> T:
    return items[0]

def create_pair(x: T, y: T) -> Tuple[T, T]:
    return (x, y)


from typing import Union, Optional, Any

value: Union[str, int] = 10  # Can be either a string or an integer
maybe_name: Optional[str] = None  # Optional value (can be None)
unknown_value: Any = input("Enter a value: ")  # Any type


# type of something


from dataclasses import dataclass
from typing import Protocol, Type

class VideoExporter(Protocol):
    """Basic representation of video exporting codec."""

    def prepare_export(self, video_data: str):
        """Prepares video data for exporting."""

    def do_export(self, folder):
        """Exports the video data to a folder."""

@dataclass
class MediaExporterFactory:
    video_class: Type[VideoExporter]