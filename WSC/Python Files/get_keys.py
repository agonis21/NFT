import pandas as pd

attributes_list = []

for i in range(1,1000):
    json_fn_i = str(i) + ".json"
    jsonfile_i = pd.read_json(json_fn_i)
    attributes_i = jsonfile_i["attributes"]

    for ob in attributes_i:
        attributes_list.append(ob["trait_type"])
        attributes_list = list(set(attributes_list))



attributes_list = list(set(attributes_list))

print(attributes_list)
print(len(attributes_list))
