import json

import pytest
from playwright.sync_api import Playwright

WEATHER_API_URL="https://api.openweathermap.org/data/2.5/weather"
CITY_NAME="Jerusalem,IL"
API_KEY="ad48510a9aed1ff96b51557d94bc5964"
UNITS="metric"
class Test_Open_Weather_Map:
    @pytest.fixture(scope="class",autouse=True)
    def setup(self,playwright:Playwright):
        global request_context
        request_context=playwright.request.new_context(base_url=WEATHER_API_URL)
        yield
        request_context.dispose()

    def test_get_request(self):
       api_paramas=dict(appid=API_KEY,q=CITY_NAME,units=UNITS)
       response=request_context.get(url="",params=api_paramas)
       result=response.json()
       print(json.dumps(result,indent=2))
       print(f"Status Code: {response.status}")
       print(f"Content Type: {response.headers['content-type']}")
       print(f"Date: {response.headers['date']}")
       assert "json" in response.headers["content-type"]

    def test_parsing_json(self):
        api_paramas = dict(appid=API_KEY, q=CITY_NAME, units=UNITS)
        response = request_context.get(url="", params=api_paramas)
        weather_data = response.json()
        print(f"Country is: {weather_data['sys']['country']}")
        print(f"Humidity is: {weather_data['main']['humidity']}")
        print(f"Temperature is: {weather_data['main']['temp']}")
        assert weather_data["sys"]["country"]=="IL"