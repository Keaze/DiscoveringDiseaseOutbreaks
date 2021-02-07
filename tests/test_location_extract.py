from locationextract.location_extract import (
    find_city,
    find_country,
)


def test_find_city():
    result = find_city("Berlin")
    assert "Berlin" in result


def test_find_city_with_two_words():
    result = find_city("San Francisco")
    assert "San Francisco" in result


def test_find_city_non_unicode():
    result = find_city("Mörön")
    assert "Moron" in result


def test_find_another_city():
    result = find_city("Vienna")
    assert "Vienna" in result


def test_find_city_in_string():
    result = find_city("The capital of this nation is Berlin")
    assert "Berlin" in result


def test_find_first_city_in_string():
    result = find_city("Paris and Berlin and Vienna")
    assert "Paris" in result


def test_find_country():
    result = find_country("Germany")
    assert "Germany" in result


def test_find_first_country():
    result = find_country("Germany and Austria")
    assert "Germany" in result


def test_with_headline():
    result = find_city("Flu outbreak in Galveston, Texas")
    assert "Galveston" in result


def test_empty_input():
    result = find_city("")
    assert result is None


def test_dont_find_city_as_nation():
    result = find_country("Berlin")
    assert result is None


def test_dont_find_nation_as_city():
    result = find_city("Germany")
    assert result is None


def test_part_of_word_is_a_city():
    result = find_city("Berlinasd")
    assert result is None
