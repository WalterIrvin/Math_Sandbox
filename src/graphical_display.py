import plotly
import plotly.graph_objs as G
import numpy

import interest_calculator

num = 15
random_x = numpy.random.randn(num)
random_y = numpy.random.randn(num)

# Create a trace
follow = G.Scatter(
    x=random_x,
    y=random_y,
    mode='markers'
)
output = [follow]

plotly.offline.plot(output, filename='basic-scatter.html')
print("testing")
