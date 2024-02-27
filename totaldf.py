import pandas as pd
csv = pd.read_csv('FF_SR_ data.csv')
df = csv[['food_category_id','SR_Component','SR Mean per 100g','FF Mean per 100g']]
df = df[df['SR_Component'].str.contains(':') == False]
df2 = pd.read_csv("FF_SR_ data.csv")
df["PC"] = abs((df2["FF Mean per 100g"]-df2["SR Mean per 100g"])/(df2["SR Mean per 100g"]))
print(df)