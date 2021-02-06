from locationextract.location_extract import extract_locations


def test_find_city():
    result = extract_locations("Berlin")
    assert "Berlin" in result

def test_find_city_with_two_words():
    result = extract_locations("San Francisco")
    assert "San Francisco" in result

def test_find_another_city():
    result = extract_locations("Vienna")
    assert "Vienna" in result


def test_find_city_in_string():
    result = extract_locations("The capital of this nation is Berlin")
    assert "Berlin" in result


def test_find_multiple_cities_in_string():
    result = extract_locations("Paris and Berlin and Vienna")
    assert "Berlin" in result
    assert "Paris" in result
    assert "Vienna" in result


def test_find_country():
    result = extract_locations("Germany")
    assert "Germany" in result


def test_find_multiple_countries():
    result = extract_locations("Germany and Austria")
    assert "Germany" in result
    assert "Austria" in result

def test_with_headlin():
    result = extract_locations("Flu outbreak in Galveston, Texas")
    assert "Galveston" in result

def test_empty_input():
    result = extract_locations("")
    assert len(result) == 0
