#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash_server import app



if 'DYNO' in os.environ:
    app_name = os.environ['DASH_APP_NAME']
else:
    app_name = 'weather-plotter'






df = pd.read_csv('Data/data.csv', header = 10, sep= ';' )
df["Date"] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour']])


layout = html.Div([
    html.Div([html.H1("Statistics")], style={'textAlign': "center"}),
    html.Div([dcc.Dropdown(id='value-selected',
                           options=[{'label': str(i), 'value': i} for i in df.columns.values[5:24]],
                           value=["Temperature  [2 m above gnd]"],
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





