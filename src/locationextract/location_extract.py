import re

import geonamescache
import unidecode


class LocationFinder():
    def __init__(self, regex):
        self.regex = regex

    def find(self, string):
        normalized_input = unidecode.unidecode(string)
        s = re.finditer(self.regex, normalized_input)
        try:
            return next(s).group()
        except StopIteration:
            return None


def create_city_finder():
    result = list(
        [unidecode.unidecode(x["name"]) for x in geonamescache.GeonamesCache().get_cities().values()]
    )
    regex_compiled = _compile_regex(result)
    return LocationFinder(regex_compiled)


def create_country_finder():
    result = list(
        [unidecode.unidecode(x["name"]) for x in geonamescache.GeonamesCache().get_countries().values()]
    )
    regex_compiled = _compile_regex(result)
    return LocationFinder(regex_compiled)


def _compile_regex(result):
    distinct_values = list(set(result))
    distinct_values.sort(key=len, reverse=True)
    regex = r"\b" + r"\b|\b".join(distinct_values) + r"\b"
    regex_compiled = re.compile(regex)
    return regex_compiled


def find_country(string):
    """
    Returns the countries listed in an input string
    :return: List of countries in the input string
    """
    return create_country_finder().find(string)


def extract_locations(string):
    """
    Extracts city and country names from an input string
    """
    return find_city(string) + find_country(string)


def find_city(string):
    """
    Returns the cities listed in an input string
    :return: List of cities in the input string
    """
    return create_city_finder().find(string)


if __name__ == "__main__":
    print(find_country("Germany"))
