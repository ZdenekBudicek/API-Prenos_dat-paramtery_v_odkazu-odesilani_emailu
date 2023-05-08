import smtplib
import requests

# API
response = requests.get(url="https://api.kanye.rest/")
data = response.json()
quote = data["quote"]

# Odesílací email
# Multik789@seznam.cz

# Přijmací email
# cgfngfvgfvgfv@gmail.com

# message = "Subject: Důležítá zpráva\n\nZdravíčko, testuju si odesílání emailů. :)"

my_email = "cgfngfvgfvgfv@gmail.com"
password = "qkfsbanoxkytbjfc"
received_email = ["Multik789@seznam.cz", "budicekz@email.cz"]

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connect:
    connect.starttls()
    connect.login(user=my_email, password=password)
    connect.sendmail(from_addr=my_email,
                     to_addrs=received_email,
                     msg=quote.encode("utf-8")
                     )
