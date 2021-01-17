import pandas as pd 
import plotly.express as px

a=pd.read_csv("Copy+of+data+-+data.csv")

fig=px.scatter(a,x="date",y="cases",color="country",title="COVID CASES")
fig.show()
