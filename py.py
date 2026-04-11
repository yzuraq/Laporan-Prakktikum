import random
import requests

url = "FORM_RESPONSE_URL"

names = ["Informatika","Sistem Informasi","Teknik Elektro","Teknik Komputer"]

for i in range(50):

    data = {
        "entry.123456789": random.choice(names)
    }

    requests.post(url, data=data)