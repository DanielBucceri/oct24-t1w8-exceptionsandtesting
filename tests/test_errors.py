import pytest
from src.errors import convert_to_integer

def  test_string():
    assert convert_to_integer(123) == 123 #must assert something to test. Assert that convert_to_integer(123) == 123

def test_float():
    with pytest.raises(ValueError):   # cant say is assert value == to exception
        convert_to_integer('12.3')    #import pytest - use with pytest.raises and pass in expected exception