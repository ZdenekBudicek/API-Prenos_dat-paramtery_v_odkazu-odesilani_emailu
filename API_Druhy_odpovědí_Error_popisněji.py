# http://api.open-notify.org/iss-now.json
# request = žádost
# response = odpověď

import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

# 1xx = ještě není konec
# 2xx = vše OK, tady máš data
# 3xx = přesměrování
# 4xx = chyba na straně uživatele
# 5xx = chyba na straně poskytovatele
