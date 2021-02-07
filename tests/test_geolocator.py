from locationextract.city import CityFromName


def test_find_country_code():
    sut = CityFromName()
    result = sut.create("Berlin").country_code
    assert result == "DE"


def test_find_another_country_code():
    sut = CityFromName()
    result = sut.create("Vienna").country_code
    assert result == "AT"


def test_find_country_code_non_unicode():
    sut = CityFromName()
    result = sut.create("Moron").country_code
    assert result == "AR"


def test_invalid_city():
    sut = CityFromName()
    result = sut.create("Asdafasgsdfgdf").country_code
    assert result is None


def test_find_geo_location():
    sut = CityFromName()
    result = sut.create("Vienna")
    assert (result.latitude, result.longitude) == (48.20849, 16.37208)


def test_get_city_object():
    sut = CityFromName()
    result = sut.create("Vienna")
    assert result.name == "Vienna"
