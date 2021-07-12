
import pandas as pd
from pandas import DataFrame as df
import plotly.graph_objects as go
import plotly.express as px
import requests
import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime
import json
from plotly.offline import plot

pd.options.display.max_columns=None
date=datetime.date.today()
dating=[]
lat=[]
lon=[]
active=[]
death=[]
recover=[]
country=[]
confirmed=[]
confirmedsize=[]
province=[]
for i in range(4):
  date=date-datetime.timedelta(1)
  d=date.strftime("%m-%d-%Y")
  url=str("https://covid19.mathdro.id/api/daily/"+str(d))
  r=requests.get(url).json()
  for x in r:
    dating.append(d)
    province.append(x["provinceState"])
    lat.append(x['lat'])
    lon.append(x['long'])
    recover.append(x["recovered"])
    death.append(x["deaths"])
    active.append(x['active'])
    country.append(x['countryRegion'])
    confirmed.append(x["confirmed"])
    confirmedsize.append(int(x["confirmed"]) // 500)
dataframe=df(list(zip(dating,province,country,lat,lon,recover,death,active,confirmed,confirmedsize)), columns =["date","province","country",'lat','lon','recover','death','active',"confirmed","confirmedsize"])
dataframe['place'] = dataframe['province'].str.cat(dataframe['country'], sep =",")
dataframe["deathsize"]=dataframe["death"].apply(lambda x:int(x)//500)
dataframe["ratio"]=dataframe["death"].astype("int32")/dataframe["confirmed"].astype("int32")
print(dataframe)

fig = px.scatter_geo(dataframe,
                     lat="lat", lon="lon", size="deathsize",
                     color="confirmedsize",
                     hover_name="place",
                     hover_data=["death","active","confirmed"],
                     animation_frame="date",
                     template='plotly_dark',
                     projection="natural earth",
                     title="COVID-19 worldwide confirmed cases over time")
fig.update_layout( margin={"r":0,"t":0,"l":0,"b":0})
print("hello")
print("bye")
fig2 = px.scatter(dataframe,x="country", y="ratio", log_y=True,
              title='Recovery and Mortality rate over the time',
              color="confirmedsize",
              animation_frame="date",
              template='plotly_dark')
fig3 = px.bar(dataframe,x="country", y="ratio", log_y=True,
              title='Recovery and Mortality rate over the time',
              color="confirmedsize",
              animation_frame="date",
              template='plotly_dark')
df=px.data.gapminder()
#fig3=px.scatter_geo(df,locations="iso_alpha",size="pop",hover_name="country")
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig),
dcc.Graph(figure=fig2),
dcc.Graph(figure=fig3)
])
if __name__ == '__main__':
    app.run_server(debug=False)