import pyowm

#  OpenWeatherMap api
owm = pyowm.OWM('d0f0941ea7c6195b5303d7bbc74a5d2a')
mgr = owm.weather_manager()

#  Determine the current temperature in a particular city
place = input("Where are you? : ")
monitoring = mgr.weather_at_place(place)
weather = monitoring.weather
temperature = weather.temperature('celsius')["temp"]
print("Current temperature in " + place + ": " + str(temperature))

#  Advice on what to dress
if temperature < 0:
    print("Dress as warmly as possible")
elif (temperature >= 0) and (temperature <= 10):
    print("Put warm clothes on but without busting")
elif (temperature > 10) and (temperature <= 20):
    print("Put light clothes on but don't overdo it")
elif (temperature > 20) and (temperature <= 30):
    print("Put light clothes on")
else:
    print("You're going to need water and a small fan")