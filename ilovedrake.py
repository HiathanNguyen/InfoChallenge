import pandas as pd
csv = pd.read_csv('FF_SR_ data.csv')
df = csv[['food_category_id','SR_Component','FF_Component','SR Mean per 100g','FF Mean per 100g']]
df["PC"] = abs((df["FF Mean per 100g"]-df["SR Mean per 100g"])/(df["SR Mean per 100g"]))
# make merge csv files with food category csv
print(df)