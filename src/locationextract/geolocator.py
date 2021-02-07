import geonamescache as gnc
import unidecode

city_accent_mapping = {
    unidecode.unidecode(x['name']): x['name'] for x in gnc.GeonamesCache().get_cities().values()
}


class City:
    def __init__(self, data):
        self.name = data["name"] if data is not None else None
        self.country_code = data["countrycode"] if data is not None else None
        self.coord = (data["latitude"], data["longitude"]) if data is not None else None

    @staticmethod
    def from_name(name: str):
        gc = gnc.GeonamesCache()
        try:
            decoded_city = city_accent_mapping[unidecode.unidecode(name)]
        except KeyError:
            return City(None)
        city_list = gc.get_cities_by_name(decoded_city)
        city_list.sort(key=lambda entry: max([y["population"] for (_, y) in entry.items()]), reverse=True)
        for (_, data) in city_list[0].items():
            return City(data)
