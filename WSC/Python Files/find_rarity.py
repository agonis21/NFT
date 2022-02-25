import pandas as pd

df = pd.read_csv("complete_metadata.csv").set_index("Index").fillna("None")

#calculate rarity of each trait
for trait in df.columns:
    item_freq = df[trait].value_counts()

    idx = 0
    for trait_value in df[trait]:
        
        if (trait_value != "") or (trait_value != "nan"):
            rarity_float = round((item_freq[str(trait_value)]*100/3333),2) 
            rarity_outof = item_freq[str(trait_value)]
            rarity_score = round(1/(float(rarity_float)/100),4)
            new_value = trait_value + \
                        "(" + str(rarity_outof) + "/3333)" +\
                        "[" + str(rarity_float) +  "%]" +\
                        "<"+ str(rarity_score) +">"

            df[trait][idx] = new_value

            idx += 1

        print(".", end="")

    print("TRAIT")

df.to_csv("complete_dataset2.csv")
print("done")
