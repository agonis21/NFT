import pandas as pd

# 'Headgear', 'Facial Hair', 'Hands', 'Mouth Accessory', 'Background', 'Hair', 'Body', 'Eyes', 'Tattoos', 'Earring', 'Clothing', 'Mouth'

items_list = [{
        'Headgear' : "",
        'Facial Hair' : "",
        'Hands' : "",
        'Mouth Accessory' : "",
        'Background' : "",
        'Hair' : "",
        'Body' : "",
        'Eyes' : "",
        'Tattoos' : "",
        'Earring' : "",
        'Clothing' : "",
        'Mouth' : ""
    }
] #skip the first entry
for i in range(1,3334):
    json_fn_i = str(i) + ".json"
    jsonfile_i = pd.read_json(json_fn_i)
    attributes_i = jsonfile_i["attributes"]
    new_attrib_i = {
        'Headgear' : "",
        'Facial Hair' : "",
        'Hands' : "",
        'Mouth Accessory' : "",
        'Background' : "",
        'Hair' : "",
        'Body' : "",
        'Eyes' : "",
        'Tattoos' : "",
        'Earring' : "",
        'Clothing' : "",
        'Mouth' : ""
    }

    for obj in attributes_i:
        #new_attrib_i.append({obj["trait_type"] : obj["value"]})
        new_attrib_i[obj["trait_type"]] = obj["value"]



    items_list.append(new_attrib_i)
    print(".", end = "")

#print(items_list)
df = pd.DataFrame(items_list)
df.to_csv("complete_metadata.csv")
print("done")
    
