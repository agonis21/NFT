import pandas as pd

df = pd.read_csv("complete_metadata.csv").set_index("Index").fillna("None")

total_rarity_list = []
for i in range(0, 10):
    total_rarity = 0

    for trait in df.columns:

        item_freq = df[trait].value_counts()

        idx = 0

        trait_value = df.iloc[i][trait]
        
        rarity_float = round((item_freq[str(trait_value)]*100/3333),2) 
        rarity_score = round(1/(float(rarity_float)/100),4)

        total_rarity += rarity_score

    total_rarity_list.append(total_rarity)

    print(".", end="")

#print(total_rarity_list)

import numpy as np

np_tlr = np.array(total_rarity_list)
for i in range(len(total_rarity_list)):
     idx = np.argmax(np_tlr)
     np_tlr[idx] = i

df["Rarity"] = np_tlr

print(df.toString())
#df.to_csv("rarity_included_metadata.csv")
    

