import requests
#Weather API (can be implemented for soccer scores as well)
#Not Working
apiKey = "0a70b2bc1fa41ca579cee4521cad06e1"
baseUrl = "https://api.openweathermap.org/data/2.5/weather"

#grab city from user input
city = input("Enter a city name: ")
requestUrl = f"{baseUrl}?appid={apiKey}&q={city}"
response = requests.get(requestUrl)
#potential error with api key // so check
