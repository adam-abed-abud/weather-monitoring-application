import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_server import app
import main


if 'DYNO' in os.environ:
    app_name = os.environ['DASH_APP_NAME']
else:
    app_name = 'weather-plotter/'

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])



layout = html.Div([
    dcc.SyntaxHighlighter(language='python',
                          children=open('main.py', 'r').read()),
])

csv_layout = html.A("View the CSV dataset",
                     href="Data/data.csv",
                     target="_blank", style={"width": "30%", "float": "right"}, className="four columns")



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname is None or pathname.replace(app_name, '').strip('/') == '':
        return main.layout
    elif pathname is None or pathname.replace(app_name, '').strip('/') == 'data':
        return csv_layout
    else:
        return layout

if __name__ == '__main__':

    app.run_server(debug=True)


