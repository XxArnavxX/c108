import pandas as pd  
import plotly.figure_factory as f

re = pd.read_csv('./data.csv')
fig = f.create_distplot([re["Height(Inches)"].tolist()], ["height"], show_hist=False)
fig.show()