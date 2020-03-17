# Weather data monitoring

#### Python web application for monitoring weather data


 - Author: **Adam Abed Abud**
 - Last update: June, 2019

Adapted from: https://github.com/plotly/simple-example-chart-apps

**Data source:** https://www.meteoblue.com
List of variable definition is also provided in the repository. 

**Technology:** Python, Dash, Plotly



# Usage
Before starting the web application make sure you have the proper requirements.

```sh
pip3 install -r requirements.txt
```

Start the Dash web application. 

```sh
python webapp.py 
```


Start firefox with the following address:
```sh
firefox 127.0.0.1:8050
```

Enjoy!


------------
Project Organization

    ├── README.md          <- README file for developers using this project.
    |
    ├── Data
    │   └──  data.csv       <- Source of Data
    │
    ├── config.py           <- Set environmental variables (optional)
    │
    ├── dash_server.py      <- Dash web server 
    │
    ├── webapp.py           <- Starts the dash web server and renders the page
    │
    └── main.py             <- Builds the html page 


--------

License
----

**Free Software!** 
For the benefit of everyone.









