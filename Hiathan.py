import pandas as pd
import plotly.express as px
csv = pd.read_csv('FF_SR_ data.csv')
df5 = csv[['food_category_id','FF Food description','FF_Component','SR Mean per 100g','FF Mean per 100g']]
df5 = df5[df5['FF_Component'].str.contains('SFA') == False]
df6 = pd.read_csv("FF_SR_ data.csv")
df5["PC"] = abs((df6["FF Mean per 100g"]-df6["SR Mean per 100g"])/(df6["SR Mean per 100g"])) * 100
LEGUME = df5[df5['food_category_id'] == 16]
LEGUME = LEGUME.sort_values(by="PC", ascending=False)
LEGUME = LEGUME[LEGUME['PC'] != 0]
LEGUME = LEGUME[LEGUME['SR Mean per 100g'] != 0]
topten = LEGUME[0:17]



fig = px.histogram(topten, y='PC', x='FF_Component', title='Percent Change in Top 10 Legume Nutrients',text_auto='.3s')
fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
fig.show()