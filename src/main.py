###### This module runs API REST calls to Spotify ######
import requests
import json

url = "https://api.spotify.com/v1/search"
request_headers = {"Authorization": "Bearer BQDgvbZBOwIitZ5otA5Xcx_8XwVjBFJXfB-R8ilPu2iWCbQ13sGaPSgoOapccUVKUk6qFtDY6P43oxSt850zesnfDyklVIcj__HgstSWj-OUvs_xc8bS9Yx2tKiHJNSN04Yd9nyhxQ"}
request_params = {"q": "supersubmarina", "type": "artist"}

response = requests.get(url, params=request_params, headers=request_headers)

#response = requests.get("https://api.spotify.com/v1/search?q=supersubmarina&type=artist", headers={"Authorization": "Bearer BQBS7qDxJ6NPobFOaEhwqQPnNlfRP8kTOvBmujUJ9OQZrCdiQ50g6uTHi5Wn7DTCJaI2PMW7xDeCSqvLHQeD61o2J_4HV_teIr0ul-Yd1v37iZiH7ESPkECAB1MHwaHeR0K37TV_Bu3VIw"})

print(response.url)
print(response.text)

print("Eeeee")
json1_data = json.loads(response.text)
print(json1_data)
print("Eeeee")
print(json1_data['artists'])