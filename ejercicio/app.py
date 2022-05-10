from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objs as go

app = Dash(__name__)

def server_layout():
    df = pd.read_excel('/vol/data.xlsx')
    return html.Div([html.H1('Blog para la comunidad UPB'),
                       html.Div('Bienvenid@s'),
                       html.Div(df['Publicación 1']),
                       html.Div(df['Publicación 2']),
                       html.Div(df['Publicación 3']),
                       html.Div(df['Publicación 4']),])

app.layout = server_layout

#funcion principal
if __name__ == '__main__':
    #cargar el objeto principal a todas las interfaces de red en el puerto 80
    app.run_server(host='0.0.0.0',port=80)