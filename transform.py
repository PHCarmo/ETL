import requests

class Transform:
    def __init__(self):
        self.HOST = "https://www.googleapis.com/customsearch/v1"
        self.ACCESS_KEY = "Insert your API key here"
        self.CONTEXT = "51275c3de2d644c29"

    def set_suggestions(self, users):
        for user in users:
            if (results := self.get_google_results(user)):
                suggestions = {}
                for item in results["items"]:
                    suggestions[item["title"]] = item["link"]
                user.suggestions = suggestions

    def get_google_results(self, user):
        params = {
            "key": self.ACCESS_KEY,
            "cx": self.CONTEXT,
            "q": f"Things to do in a {user.weather} day in {user.get_location()}",
        }
        response = requests.get(
            f'{self.HOST}',
            params=params
        )
        return response.json() if response.status_code == 200 else None