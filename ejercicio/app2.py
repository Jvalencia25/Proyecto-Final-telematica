#Llamar librerias
from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objs as go 

#Declarar objetos principales
app = Dash(__name__)
#Cargar base de datos
df = pd.read_excel('data.xlsx')
#configurar el sitio web
app.layout = html.Div([html.H1('Programa para covin en medallo city (y alrededores)'),
                       html.Div('Información de la pagina y pues eso'),
                       dcc.Graph(id= 'mapa',figure={
                           
                       })])
#Funcion principal
if __name__== '__main__':
    #cargar el objeto principal a todas las interfaces de red en el puerto 80
    app.run_server(host='0.0.0.0',port=80)