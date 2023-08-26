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

    def get_weather(self):
        return self.weather or "Not Found"

    def get_temperature(self):
        return self.temperature or "Not Found"

    @property
    def suggestions(self):
        return self.__suggestions

    @suggestions.setter
    def suggestions(self, val):
        self.__suggestions = val