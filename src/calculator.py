# app.py
# This is a test commit
import pytest
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


def test_add():
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(2, 4) == 6
    assert add(5, 6) == 11

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(10, 5) == 5
    assert subtract(20, 10) == 10

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(8, 10) == 80
    assert multiply(80, 10) == 800

def test_divide():
    assert divide(6, 3) == 2
    assert divide(8, 2) == 4


