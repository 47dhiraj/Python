from typing import Union, List, Optional


'''
    Type hint like 'Union' for indicating that a parameter can be of multiple types.
    
    Type hint like 'Optional' for indicating that a parameter can be of a specific type or None.
    
    Type hints like 'List' for indicating a list of a specific type.


    Note: Remember that type hinting is primarily for documentation and static code analysis, 
    and Python is still dynamically typed, so the type hints won't prevent you from running the code with different types. 
    
    However, tools like 'mypy' can perform static type checking based on your type hints.
        ==> pip install mypy
        And, also install vscode 'mypy' extension

'''


def greet_user(name: str, age: Optional[int] = None) -> str:    # age ko default value None  and  -> str vannale function ko return type string ho
    if age is None:
        return f"Hello, {name}!"
    else:
        return f"Hello, {name}! You are {age} years old."


def get_max_value(a: int, b: int) -> int:
    return a if a > b else b
    

def combine_strings(strings: List[str], separator: str = ' ') -> str:
    return separator.join(strings)


def process_data(data: Union[str, List[int]]) -> None:
    if isinstance(data, str):
        print(f"Processing string: {data}")
    elif isinstance(data, list):
        print("Processing list of integers:")
        for item in data:
            print(item)


user_greeting = greet_user("Agent47", 27)
print(user_greeting)

max_val = get_max_value(10, 15)
print(f"The maximum value is: {max_val}")

names = ["Alice", "Bob", "Charlie"]
combined = combine_strings(names, ', ')
print(combined)

process_data("Some text data")
process_data([1, 2, 3, 4, 5])
