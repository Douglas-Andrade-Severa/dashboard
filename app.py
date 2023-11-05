import dash 
from dash import dcc, html
from dash import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd
import yfinance as yf

#ler e ajustar os dados

#acoes_b3 = ['PETR4.SA',#PETROBRAS
#            'VALE3.SA',#VALE
#            'ITUB4.SA',#ITAU
#            'BBDC4.SA',#BB
#            'ABEV3.SA',#AMBEV
#            'B3SA3.SA',#B3
#            'MRFG3.SA',#MARFRIG
#            'WEGE3.SA',#WEG
#            'SUZB3.SA',#SUZANO
#            'VIVT3.SA',#VIVO
#            '^BVSP']   #INDICE IBOVESPA


#df = yf.download(acoes_b3, period='1y')
#df.index.name = None
#df.to_csv('b3.csv')
data = pd.read_csv('b3.csv', index_col=0)

#Contrução do gráfico

data2 = data['VALE3.SA']
fig2  = px.line(data2)
fig2.update_layout(title='VALE3.SA',
                   yaxis_title='Preço (R$)',
                   xaxis_title='Data',
                   template='plotly_dark',
                   showlegend=False) #plotly.com/python/templates

data3 = data['ITUB4.SA']
fig3  = px.line(data3)
fig3.update_layout(title='ITUB4.SA',
                   yaxis_title='Preço (R$)',
                   xaxis_title='Data',
                   template='plotly_dark',
                   showlegend=False) #plotly.com/python/templates


data4 = pd.read_csv('petro.csv', index_col=0)
candle = go.Candlestick(x=data4.index,
                        open=data4['Open'],
                        high=data4['High'],
                        low=data4['Low'],
                        close=data4['Close'])

fig4 = go.Figure(data=candle)
fig4.update_layout(title='Ações da petrobras',
                   yaxis_title='Preço (R$)',
                   xaxis_title='Data',
                   template='plotly_dark') #plotly.com/python/templates

#Inicialização da aplicação
app =  dash.Dash(__name__,
                 external_stylesheets=[dbc.themes.CYBORG]) #bootswatch.com/

#Layout do dashboard
app.layout = dbc.Container([#dash-bootstrap-components.opensource.faculty.ia/docs/components
    dbc.Row([
        dbc.Col([
            html.H1('Dashboard de Mercado Financeiro',
                    className='text-center text-primary'),# dash.plotly.com/dash-html-components
            html.Br()
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='menu', value=['ABEV3.SA'],
                        options={x:x for x in data.columns},
                        multi=True),
            dcc.Graph(id='grafico')
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig2)
        ], width=4),
        dbc.Col([
            dcc.Graph(figure=fig3)
        ], width={'size':'8'})
    ], className='g-0'),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig4)
        ])
    ])
])


# Callbacks
@app.callback(
    Output('grafico','figure'),
    Input('menu', 'value')
)
def funcao(acoes):
    data_fig = data[acoes]
    fig  = px.line(data_fig)
    fig.update_layout(title='B3 10+',
                    yaxis_title='Preço (R$)',
                    xaxis_title='Data',
                    template='plotly_dark',
                    showlegend=False) #plotly.com/python/templates
    return fig
    

#Execução da aplicação
if __name__ == '__main__':
    app.run_server(debug=True)