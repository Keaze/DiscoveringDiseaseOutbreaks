import geonamescache as gnc
import unidecode


class CityFactory():
    def __init__(self):
        self.city_accent_mapping = {
            unidecode.unidecode(x['name']): x['name'] for x in gnc.GeonamesCache().get_cities().values()
        }
        self.gc = gnc.GeonamesCache()

    def from_name(self, name: str):
        if name is None:
            return City(None)
        try:
            decoded_city = self.city_accent_mapping[unidecode.unidecode(name)]
        except KeyError:
            return City(None)
        city_list = self.gc.get_cities_by_name(decoded_city)
        city_list.sort(key=lambda entry: max([y["population"] for (_, y) in entry.items()]), reverse=True)
        for (_, data) in city_list[0].items():
            return City(data)

class City:
    def __init__(self, data):
        self.name = data["name"] if data is not None else None
        self.country_code = data["countrycode"] if data is not None else None
        self.latitude = data["latitude"] if data is not None else None
        self.longitude = data["longitude"] if data is not None else None

    def __str__(self) -> str:
        return f"{self.name} - {self.country_code}"

    def __repr__(self) -> str:
        return self.__str__()

    def df_data(self):

        return self.name, self.country_code, self.latitude, self.longitude

