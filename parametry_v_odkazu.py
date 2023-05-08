import requests

# parametr v odkazu
# language = en, es, fr, cs

# 1. Ruční zadání

# response = requests.get("https://evilinsult.com/generate_insult.php?lang=cs&type=json")
# response.raise_for_status()
# print(response.text)
# data = response.json()
#
# print(data["insult"])

# 2. Pomocí proměnné
# language = "en"
#
# response = requests.get(f"https://evilinsult.com/generate_insult.php?lang={language}&type=json")
# response.raise_for_status()
# data = response.json()
# print(data["insult"])

# 3. Pomocí dictionary (Nejpoužívanější a nejlepší)
my_parameters = {
    "lang": "es",
    "type": "json"
}
response = requests.get(f"https://evilinsult.com/generate_insult.php", params=my_parameters)
response.raise_for_status()
data = response.json()

print(data["insult"])
