import pandas as pd
import plotly.express as px
csv = pd.read_csv('FF_SR_ data.csv')
df = csv[['food_category_id','FF Food description','FF_Component','SR Mean per 100g','FF Mean per 100g']]
dict = {}
for index, row in df.iterros():
    dict[row[]]













df = df[df['FF_Component'].str.contains('SFA') == False]

df2 = pd.read_csv("FF_SR_ data.csv")
df["PC"] = abs((df2["FF Mean per 100g"]-df2["SR Mean per 100g"])/(df2["SR Mean per 100g"])) * 100


DAIRY = df[df['food_category_id'] == 1]
DAIRY = DAIRY.sort_values(by="PC", ascending=False)
DAIRY = DAIRY[DAIRY['PC'] != 0]

DAIRY = DAIRY[DAIRY['SR Mean per 100g'] != 0]

print(DAIRY['FF_Component'].value_counts())
