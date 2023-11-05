import dash
from dash import dcc, html
from dash import Input, Output, State

#Iniciar a aplicação
app = dash.Dash(__name__)

#Estrutura da aplicação
app.layout = html.Div(children=[
    html.H2(children='Atualiza valor do texto!'),
    html.Br(),
    'Entrada: ', dcc.Input(id='entrada', value='Valor Inicial'),
    html.Button(id='botao', n_clicks=0, children='Aciona collback'),
    html.Br(),
    html.H4(id='saida', children='')
])

#Callbacks (https://dash.plotly.com/advanced-callbacks)
@app.callback(
    Output(component_id='saida', component_property='children'),
    State(component_id='entrada', component_property='value'),
    Input(component_id='botao', component_property='n_clicks')
)

def funcao(a, clicks):
    if clicks > 0:
        b = f'Texto inserido: {a}'
        return b
    else:
        raise dash.exceptions.PreventUpdate

#Execução do aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)