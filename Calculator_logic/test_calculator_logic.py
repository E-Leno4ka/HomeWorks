import calculator_logic as c
import pytest

def test_add():
    assert c.add(10, 5) == 15
    assert c.add(-1, 1) == 0
    assert c.add(-1, -1) == -2
    with pytest.raises(TypeError):
        c.add("text", 1)
    with pytest.raises(TypeError):
        c.add(1, "text")

def test_subtract():
    assert c.subtract(10, 5) == 5
    assert c.subtract(-1, 1) == -2
    assert c.subtract(-1, -1) == 0
    with pytest.raises(TypeError):
        c.subtract("text", 1)
    with pytest.raises(TypeError):
        c.subtract(1, "text")

def test_multiply():
    assert c.multiply(10, 5) == 50
    assert c.multiply(-1, 1) == -1
    assert c.multiply(-1, -1) == 1

def test_divide():
    assert c.divide(10, 2) == 5
    assert c.divide(-10, 2) == -5
    assert c.divide(10, -2) == -5
    
    with pytest.raises(TypeError):
        c.divide("text", 1)
    with pytest.raises(TypeError):
        c.divide(1, "text")
    with pytest.raises(ZeroDivisionError):
        c.divide(10, 0)


def test_square():
    assert c.square(5) == 25
    assert c.square(-7) == 49
    assert c.square(1) == 1
    assert c.square(-1) == 1
    assert c.square(0) == 0


test_add()
test_subtract()
test_multiply()
test_divide()
test_square()
print("Все тесты пройдены успешно!")

