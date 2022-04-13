import requests


def get_json_from_api():
    lat = 43.0667
    lan = 76.9167
    api_key = "530327497eaee1ce46e9d8b817857dd4"
    api_call = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lan, api_key)
    result = requests.get(api_call)
    json_res = result.json()

    return json_res


a = get_json_from_api()
print(a)
