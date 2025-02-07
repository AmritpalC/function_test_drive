# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._


```python
# EXAMPLE

def includes_todo(string):
    """Returns a boolean depending on if the string contains '#TODO'

    Parameters: (list all parameters and their types)
        string: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        Boolean -> depending on if the string contains '#TODO'

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
An empty string
It returns False
"""
includes_todo("") => False

"""
No #TODO in string
It returns False
"""
includes_todo("HELLO WORLD") => False

"""
Has a #TODO in the line
It returns True
"""
includes_todo("#TODO learn Python") => True

"""
Lower case #todo
It returns False
"""
includes_todo("#todo is not good enough") => False

"""
Given #TODO as part of a word, e.g. #TODO!!
It returns False
"""
includes_todo("#TODO!!") => False

"""
Given a None value
It throws an error
"""
includes_todo(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.includes_todo import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_includes_todo():
    result = includes_todo("#TODO")
    assert result == True
```

Ensure all test function names are unique, otherwise pytest will ignore them!
