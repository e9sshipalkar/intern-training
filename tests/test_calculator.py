from calculator import add 

def test_add_two_numbers():
    result = add (2,3)
    assert result == 5

def test_add_positive_numbers():
    result = add (10, 20)
    assert result == 30 

def test_add_zero():
    result = add (0, 5)
    assert result == 5

def test_add_negative_numbers():
    result = add (-2, -3)
    assert result == -5

def test_add_floats():
    result = add (2.5, 3.5)
    assert result == 6.0

def test_add_single_numbers():
    result = add (1, 0)
    assert result == 1

def test_add_very_large_numbers():
    result = add (1000000000, 2000000000)
    assert  result == 3000000000

def test_add_strings():
    result = add( "Helllo", "Worldd") 
    assert result == "HellloWorldd" 

def test_add_special_characters():
    result = add("@#", "$%") 
    assert result == "@#$%"

def test_add_very_long_strings():
    text = "a" * 10000
    result= add(text, text)
    assert result == text + text 