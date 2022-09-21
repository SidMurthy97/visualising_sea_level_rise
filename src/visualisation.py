from sealevel_rise import apply_sea_level,find_underwater_states
import numpy as np
import pandas as pd


from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import CustomJS, Slider
from bokeh.plotting import ColumnDataSource, figure, show

topography = np.array([[1,1,0,-1,1,1,1],
                       [1,1,2,3,4,3,1],
                       [2,3,1,0,3,4,3],
                       [1,0,1,1,3,2,3],
                       [0,-1,-2,1,3,3,2],
                       [2,3,-1,1,3,0,-1],
                       [2,3,0,1,3,-1,0]])

sealevel = 1
new_topography = apply_sea_level(sealevel, topography)
connected = find_underwater_states(new_topography)

p = figure()

# must give a vector of image data for image parameter
p.image(image=[connected], x=0, y=0, dw=2, dh=2, palette="Spectral11")
show(p)