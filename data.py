import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly

df = pd.read_csv("C:/Users/Admin/OneDrive/Desktop/Python/Pro-108/project-files/data.csv")

#fig = ff.create_distplot([df["Height"].tolist()],["Height"], show_hist = False)
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Average Rating"], colors = ['red'])
plotly.offline.plot(fig)