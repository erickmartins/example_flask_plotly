from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.graph_objs as go
import numpy as np

app = Flask(__name__)

def create_plot():
    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe
    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/')
def index():
    bar = create_plot()
    return render_template('index.html', plot=bar)

