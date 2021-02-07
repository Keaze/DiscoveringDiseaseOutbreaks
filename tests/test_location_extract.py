from locationextract.location_extract import (
    extract_locations,
    find_cities,
    find_countries,
)


def test_find_city():
    result = find_cities("Berlin")
    assert "Berlin" in result


def test_find_city_with_two_words():
    result = find_cities("San Francisco")
    assert "San Francisco" in result


def test_find_another_city():
    result = find_cities("Vienna")
    assert "Vienna" in result


def test_find_city_in_string():
    result = find_cities("The capital of this nation is Berlin")
    assert "Berlin" in result


def test_find_multiple_cities_in_string():
    result = find_cities("Paris and Berlin and Vienna")
    assert "Berlin" in result
    assert "Paris" in result
    assert "Vienna" in result


def test_find_country():
    result = find_countries("Germany")
    assert "Germany" in result


def test_find_multiple_countries():
    result = find_countries("Germany and Austria")
    assert "Germany" in result
    assert "Austria" in result


def test_with_headline():
    result = find_cities("Flu outbreak in Galveston, Texas")
    assert "Galveston" in result


def test_empty_input():
    result = extract_locations("")
    assert len(result) == 0


def test_dont_find_city_as_nation():
    result = find_countries("Berlin")
    assert "Berlin" not in result


def test_dont_find_nation_as_city():
    result = find_cities("Germany")
    assert "Germany" not in result


def test_part_of_word_is_a_city():
    result = find_cities("Berlinasd")
    assert "Berlin" not in result
