import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

# json je přenos dat, zmenšuje je jejich objem a tudíž je přenos rychlejší
data = response.json()
print(data)
print(data["iss_position"])
longitude = (data["iss_position"]["longitude"])
latitude = (data["iss_position"]["latitude"])

print(f"Současná zeměpisná šířka ISS je: {latitude}")
print(f"Současná zeměpisná šířka ISS je: {longitude}")
