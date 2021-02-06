import geonamescache
import re


def find_countries(string):
    """
    Returns the countries listed in an input string
    :return: List of countries in the input string
    """
    result = list(
        [x["name"] for x in geonamescache.GeonamesCache().get_countries().values()]
    )
    distinct_countries = list(set(result))
    regex = "|".join(distinct_countries)
    regex_compiled = re.compile(regex)
    s = re.finditer(regex_compiled, string)
    return list(x.group() for x in s)


def extract_locations(string):
    """
    Extracts city and country names from an input string
    """
    return find_cities(string) + find_countries(string)


def find_cities(string):
    """
    Returns the cities listed in an input string
    :return: List of cities in the input string
    """
    result = list(
        [x["name"] for x in geonamescache.GeonamesCache().get_cities().values()]
    )
    distinct_cities = list(set(result))
    regex = "|".join(distinct_cities)
    regex_compiled = re.compile(regex)
    s = re.finditer(regex_compiled, string)
    return list(x.group() for x in s)


if __name__ == "__main__":
    print(find_countries("Germany"))
