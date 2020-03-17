#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Author: Adam Abed Abud
Mail: aaadam94@gmail.com
Adapted from @divyachandran. Thank you!
Last modified: June 10, 2019
"""

import dash

app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True
