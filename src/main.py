###### This module runs API REST calls to Spotify ######
import requests
import json

url = "https://api.spotify.com/v1/search"
request_headers = {"Authorization": "Bearer BQBUJKdeINi1J77Hcn1OKkuG_8hB4WNEeVmsxLUIccRJ_zkzITibR7ptNjrZJwPglbj97j3aA0sVpc2t9_8tyZ6jg35_IJY1K_ug2kRonBwYq8GNfyFv3uC4BQkkyvnz4pUCZPRM7bHylA"}
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