import locationextract.city as gl
from locationextract.city import City


def test_find_country_code():
    result = City.from_name("Berlin").country_code
    assert result == "DE"


def test_find_another_country_code():
    result = City.from_name("Vienna").country_code
    assert result == "AT"


def test_find_country_code_non_unicode():
    result = City.from_name("Moron").country_code
    assert result == "AR"


def test_invalid_city():
    result = City.from_name("Asdafasgsdfgdf").country_code
    assert result is None


def test_find_geo_location():
    result = City.from_name("Vienna").coord
    assert result == (48.20849, 16.37208)


def test_get_city_object():
    sut = gl.City.from_name("Vienna")
    assert sut.name == "Vienna"
