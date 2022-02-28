import pandas as pd
import numpy as np
import re



all_items = np.array(pd.read_json("all_items.json"))
new_items = []


for i in range(len(all_items)):
    item_no = int(re.search(r'\d+', all_items[i][1]).group())
    item_rank = int(re.search(r'\d+', all_items[i][0]).group())
    new_items.append([item_no, item_rank])



df = pd.read_csv("rarity_metadata.csv").set_index("Index").fillna("None")
#print(df.iloc[9])

for item in new_items:
    item_no = item[0]
    item_rank = item[1]
    
    df.at[item_no, "RT_Rarity"] = item_rank

    print(df.iloc[item_no]["RT_Rarity"])

df.to_csv("rt_rarity_metadata.csv")
