class User:
    def __init__(self, *args, **kwargs):
        self.weather = args[0]
        self.temperature = kwargs.get('temperature')
        self.location = kwargs.get('name')
        self.region = kwargs.get('region')
        self.country = kwargs.get('country')
        self.suggestions = None

    def get_location(self):
        return self.location or self.region or self.country or "Not Found"

    @property
    def weather(self):
        return self.__weather

    @weather.setter
    def weather(self, val):
        self.__weather = val

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, val):
        self.__temperature = val

    @property
    def suggestions(self):
        return self.__suggestions

    @suggestions.setter
    def suggestions(self, val):
        self.__suggestions = val