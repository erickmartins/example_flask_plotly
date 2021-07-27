from flask import Flask, render_template
import pandas as pd
import json
import plotly
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import numpy as np

app = Flask(__name__)

def get_data(n):
    x = np.linspace(0, 1, n)
    y = np.random.randn(n)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe
    return df

def create_plot():
    N = 40
    df1 = get_data(N)
    df2 = get_data(N)
    df3 = get_data(N)
    fig = make_subplots(rows=2, cols=2,specs=[[{}, {}],[{'colspan': 2}, None]])    
    fig.add_bar(x=df1['x'],y=df1['y'], row=1, col=1)
    fig.add_bar(x=df2['x'],y=df2['y'], row=1, col=2)
    fig.add_bar(x=df3['x'],y=df3['y'], row=2, col=1)
    fig.update_layout(height=800)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/')
def index():
    bar = create_plot()
    return render_template('index.html', plot=bar)

