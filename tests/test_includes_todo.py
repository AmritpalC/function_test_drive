from lib.includes_todo import *
# EXAMPLE

"""
An empty string
It returns False
"""
# includes_todo("") => False
def test_empty_line():
    result = includes_todo("")
    assert result == False

"""
No #TODO in string
It returns False
"""
# includes_todo("HELLO WORLD") => False
def test_no_todo_in_line():
    result = includes_todo("Drink tea")
    assert result == False


"""
Has a #TODO in the line
It returns True
"""
# includes_todo("#TODO learn Python") => True
def test_line_includes_todo():
    result = includes_todo("#TODO turn the heating on!")
    assert result == True

"""
Lower case #todo
It returns False
"""
# includes_todo("#todo is not good enough") => False
def test_lower_case_todo():
    result = includes_todo("lower case is #todo")
    assert result == False

"""
Given #TODO as part of a word, e.g. #TODO!!
We want it to return True
"""
# includes_todo("#TODO!!") => True
def test_todo_as_part_of_longer_word():
    result = includes_todo("#TODO!! Have a drink 🍷")
    assert result == True
