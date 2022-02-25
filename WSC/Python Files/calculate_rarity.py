import pandas as pd

df = pd.read_csv("complete_metadata.csv").set_index("Index").fillna("None")

def calc_rarity(n):
    total_rarity = 0

    for trait in df.columns:

        item_freq = df[trait].value_counts()

        idx = 0

        trait_value = df.iloc[n][trait]
        
        rarity_outof = "(" + str(item_freq[trait_value]) + "/3333)"
        rarity_float = round((item_freq[str(trait_value)]*100/3333),2) 
        rarity_score = round(1/(float(rarity_float)/100),4)

        total_rarity += rarity_score

        print(trait + ":", trait_value,
              rarity_outof,
              str(rarity_float) + "%",
              "<" + str(rarity_score) + ">")


    print(total_rarity)

    return total_rarity
