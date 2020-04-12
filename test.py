import requests
import json
import time
from collections import defaultdict
from io import StringIO
import numpy as np
import pandas as pd
import logging
import numpy
import matplotlib.pyplot as plt
import sys
import csv
# import datetime
logging.basicConfig(level=logging.DEBUG)
import COVID19Py
import matplotlib

import googlemaps
from datetime import datetime

from bokeh.plotting import figure, output_file, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, line_width=2)

# show the results
show(p)