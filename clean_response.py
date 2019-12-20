import ast
import json
import requests

with open('json_list.txt','r') as f:
    json_list_raw = f.read()

with open('json_list2.txt','r') as f:
    json_list_raw2 = f.read()
#print(json_list)
#print(json_list)

#print(len(json_list))
print(type(json_list_raw))

json_list = ast.literal_eval(json_list_raw)
json_list2 = ast.literal_eval(json_list_raw2)

print(type(json_list))

print(len(json_list))

missing_nums_set = set(i for i in range(1,613))
clean_json_list = []
for sub in json_list:
    print(type(sub))
    d = json.loads(sub)
    try: 
        if d['success'] == False:
            print("do nothing")
    except:
        clean_json_list.append(d)
    try:
        cur_page=(d['currentPage'])
        missing_nums_set.remove(cur_page)
    except:
        print("skipping")

print(missing_nums_set)

for sub in json_list2:
    print(type(sub))
    d = json.loads(sub)
    clean_json_list.append(d)

    try:
        cur_page=(d['currentPage'])
        missing_nums_set.remove(cur_page)
    except:
        print("skipping")

with open('clean_json_list.txt','w') as f:
    f.write(str(clean_json_list))