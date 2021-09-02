import pandas as p
import plotly.express as px
import csv

df = p.read_csv("data.csv")
fig = px.scatter(df,x = "student_id", y= "level", color= "attempt",size_max = 60,title="attempt of student")
fig.show()