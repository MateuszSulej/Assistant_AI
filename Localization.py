import requests


def get_location():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Błąd przy pobieraniu lokalizacji: {e}")
        return None


def locationData():
    location_data = get_location()
    if location_data:
        city = location_data.get("city")
        region = location_data.get("region")
        country = location_data.get("country")
        return city, region, country
