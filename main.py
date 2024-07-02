import requests
from datetime import datetime
import smtplib as em
import time


MY_LAT = 11.924229 # Your latitude
MY_LONG = 79.626022 # Your longitude
start = True
while start:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_longitude)
    print(iss_latitude)


    if MY_LAT-5 < iss_latitude < MY_LAT+5 and MY_LONG-5 < iss_longitude < MY_LONG+5:

        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.utcnow()
        hr = time_now.hour
        print(hr)
        # print(sunset)
        if hr >= sunset or hr <= sunrise:
            connection = em.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user="Your User Name", password="Your Password")
            connection.sendmail(from_addr="azhagesan807@gmail.com",
                                to_addrs="azhagesany@gmail.com",
                                msg="Subject:ISS is above your head\n\n check out the night sky")

            start = False
            connection.close()

    time.sleep(60)

