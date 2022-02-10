import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Import csv file containing match events
df_events = pd.read_csv('events.csv')
df_events.rename(columns={'hitter_x':'hitter_y','hitter_y':'hitter_x','receiver_x':'receiver_y','receiver_y':'receiver_x'},inplace=True)

# Set scaling factor for tennis court coordinates
scale = 0.3048

# Initiate Figure
fig = go.Figure()

# Create Dash App
app = dash.Dash(__name__)

app.layout = html.Div([
        dcc.Graph(id='graph-with-slider',figure=fig,animate=True),
        dcc.Slider(id='slider',min=1,max=11,value=9,step=None,
                   marks={1:'rally 1',2:'rally 2',3:'rally 3',4:'rally 4',5:'rally 5',6:'rally 6',
                          7:'rally 7',8:'rally 8',9:'rally 9',10:'rally 10',11:'rally 11'})
        ])

@app.callback(Output('graph-with-slider','figure'),
              [Input(component_id='slider',component_property='value')])

def update_output(value):
    df_rally = df_events[df_events['rallyid']==value].copy()
    x_loc = df_rally['hitter_x'].values
    y_loc = df_rally['hitter_y'].values
    winner = df_rally['hitter'].values[-1]
    server = df_rally['hitter'].values[0]

    # Add scatter, layout and set frames
    fig.add_trace(
        go.Scatter(x=[], y=[], mode='markers', marker=dict(color='royalblue', size=8)))

    fig.layout = go.Layout(
        title=f"RallyId no {value} serving {server} and rally winnner is {winner}",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None, {'frame': {'duration': 800}, 'transition': {'duration': 3000}}])])]
    )

    fig.frames = [go.Frame(data=[
        go.Scatter(x=[x_loc[i]], y=[y_loc[i]], mode='markers', marker=dict(color='royalblue', size=8))]) for
        i in range(len(x_loc))]

    # Plot tennis court
    # Draw outer sidelines
    fig.add_shape(type="rect",
                  xref="x", yref="y",
                  x0=0 * scale, x1=78 * scale, y0=0 * scale, y1=36 * scale,
                  line=dict(color='white', width=3),
                  fillcolor='lightblue', opacity=0.2)

    # Draw inner sidelines
    fig.add_shape(type="rect",
                  xref="x", yref="y",
                  x0=0 * scale, x1=78 * scale, y0=4.5 * scale, y1=31.5 * scale,
                  line=dict(color='white', width=3))

    # Draw middle line
    fig.add_shape(type="line",
                  x0=39 * scale, y0=0 * scale, x1=39 * scale, y1=36 * scale,
                  line=dict(color='white', width=3, dash='dot'))

    # Draw left service lane
    fig.add_shape(type="line",
                  x0=19.5 * scale, y0=4.5 * scale, x1=19.5 * scale, y1=31.5 * scale,
                  line=dict(color='white', width=3))

    # Draw right service lane
    fig.add_shape(type="line",
                  x0=58.5 * scale, y0=4.5 * scale, x1=58.5 * scale, y1=31.5 * scale,
                  line=dict(color='white', width=3))

    # Draw center service line
    fig.add_shape(type="line",
                  x0=19.5 * scale, y0=18 * scale, x1=58.5 * scale, y1=18 * scale,
                  line=dict(color='white', width=3))

    fig.update_layout(width=1000,height=461,xaxis_range=(-14 * scale, 96 * scale),
                      yaxis_range=(-10 * scale, 46 * scale),xaxis_showgrid=False, yaxis_showgrid=False)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)


