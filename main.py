import pandas as pd
import statistics
import plotly.express as px

df = pd.read_csv("savings_data_final.csv")
fig = px.scatter(df, y="quant_saved", color="rem_any")
fig.show()
