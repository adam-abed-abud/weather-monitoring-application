#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash_server import app
import glob
import datetime


if 'DYNO' in os.environ:
    app_name = os.environ['DASH_APP_NAME']
else:
    app_name = 'weather-plotter'



def time_to_date(timestamp):
    year = int(timestamp[0:4])
    month = int(timestamp[4:6])
    day = int(timestamp[6:8])
    hour = int(timestamp[9:11])
    #minute = int(timestamp[11:13])
    #print("year {}".format(timestamp[0:4]))
    #print("month {}".format(timestamp[4:6]))
    #print("day {}".format(timestamp[6:8]))
    #print("hour {}".format(timestamp[9:11]))  
    #print("minute {}".format(timestamp[11:13]))    
    
    return datetime.datetime(year, month, day, hour)

def return_year(timestamp):
    year = int(timestamp[0:4])
    return year

def return_month(timestamp):
    month = int(timestamp[4:6])    
    return month

def return_day(timestamp):
    day = int(timestamp[6:8])
    return day

def return_hour(timestamp):
    hour = int(timestamp[9:11])
    return hour


path = r'Data/combined'  
#all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent
#df_from_each_file = (pd.read_csv(f, header = 10, sep= ';') for f in all_files)

## the following two work for the new format without year, month, date, time
all_files = glob.glob(os.path.join(path, "w*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent
df_from_each_file = (pd.read_csv(f, header = 9, sep= ',') for f in all_files)
df = pd.concat(df_from_each_file, ignore_index=True, sort=True)  

#df["timestamp"].map(str).apply(time_to_date)


#df = pd.read_csv('Data/data.csv', header = 10, sep= ';' )



df["Year"] = df["timestamp"].map(str).apply(return_year)
df["Month"] = df["timestamp"].map(str).apply(return_month)
df["Day"] = df["timestamp"].map(str).apply(return_day)
df["Hour"] = df["timestamp"].map(str).apply(return_hour)
df["Date"] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour']])
#df["Date"] = df["timestamp"].map(str).apply(time_to_date)
df.sort_values(by=['Date'], inplace=True, ascending=False)

#print(df['Date'].to_string())

layout = html.Div([
    html.Div([html.H1("Data viewer")], style={'textAlign': "center"}),
    html.Div([dcc.Dropdown(id='value-selected',
                           options=[{'label': str(i), 'value': i} for i in df.columns.values[5:24]],
                           value=["Geneva Temperature"],
                           multi=True,
                           style={"display": "block", "margin-left": "auto", "margin-right": "auto", "width": "100%"},
                           className="eight columns"),
              html.A("View the CSV dataset",
                     href="./data",
                     target="_blank", style={"width": "30%", "float": "right"}, className="four columns")],
             className="row"),
    dcc.Graph(id="my-graph"),
    html.Div([dcc.RangeSlider(id='month-selected', min=1, max=12, step=1,
                              marks={1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}, value=[5, 6])])
], className="container")


@app.callback(dash.dependencies.Output("my-graph", "figure"), [dash.dependencies.Input("month-selected", "value"), dash.dependencies.Input("value-selected", "value")])
def update_graph(selected1, selected2):
    dff = df[(df["Month"] >= selected1[0]) & (df["Month"] <= selected1[1])]
    trace = []
    for indicator in selected2:
        trace.append(go.Scatter(x=dff.Date, y=dff[indicator], name=indicator, mode="lines",
                                marker={'size': 15, 'line': {'width': 0.2, 'color': 'white'}}, ))

    return {"data": trace, "layout": go.Layout(title="Weather Data",
                                               xaxis={"title": "Date"}, yaxis={"title": "Value"},
                                               colorway=["#C7037A","#A8AE0B", "#FFCB00", "#FF7C00", "#2F9609",
                                                         "#0E4770",  "#E20048"])}





