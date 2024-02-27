import pandas as pd
csv = pd.read_csv('FF_SR_ data.csv')
df = csv[['food_category_id','SR Food description','SR_Component','SR Mean per 100g','FF Mean per 100g']]
df = df[df['SR_Component'].str.contains('SFA') == False]

df2 = pd.read_csv("FF_SR_ data.csv")
df["PC"] = abs((df2["FF Mean per 100g"]-df2["SR Mean per 100g"])/(df2["SR Mean per 100g"])) * 100


DAIRY = df[df['food_category_id'] == 1]
DAIRY = DAIRY.sort_values(by="PC", ascending=False)
DAIRY = DAIRY[DAIRY['PC'] != 0]
#DAIRY = pd.isnull(DAIRY[DAIRY['PC'] == False])

DAIRY = DAIRY[DAIRY['SR Mean per 100g'] != 0]


print(DAIRY[0:10])