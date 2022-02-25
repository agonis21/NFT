from urllib.request import urlopen, Request
import json

url = "https://cczlwgg.mypinata.cloud/ipfs/QmY7PJQV4Cu3CUZ36LJZJczPbi8pCK6szuoWWod7BhTrWu/"

for i in range(6879,10000):
    url_i = url + str(i) + ".json"
    json_filename = str(i) + ".json"

    req = Request(url_i, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req).read()
    data = json.loads(response.decode('utf-8'))

    print(i)

    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
