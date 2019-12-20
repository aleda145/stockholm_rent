import requests
json_list = []

for i in range(1,614):
    print(i)
    r = requests.post('https://api.qasa.se/v1/homes/filter?areaId=56&page='+str(i))
    json_list.append(r.text)
    
with open('json_list.txt','w') as f:
    f.write(str(json_list))