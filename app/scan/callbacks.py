# from datetime import datetime as dt

from dash.dependencies import Input, Output  # , State
from flask_login import current_user
# import pandas_datareader as pdr


def register_callbacks(dashapp):
    # @dashapp.callback(
    #     Output('my-graph', 'figure'),
    #     Input('data-scope', 'value'),
    #     State('user-store', 'data')
    # )
    # def update_graph(selected_dropdown_value, data) -> dict:
    #     df = pdr.get_data_yahoo(selected_dropdown_value, start=dt(2017, 1, 1), end=dt.now())
    #     return {'data': [{'x': df.index, 'y': df.Close}], 'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}}

    @dashapp.callback(Output('user-store', 'data'), Input('data-scope-dropdown-menu', 'children'))
    def cur_user(children) -> str:
        if current_user.is_authenticated:
            return current_user.username

    @dashapp.callback(
        Output('username', 'children'),
        Input('user-store', 'data')
    )
    def username(data) -> str:
        if data is None:
            return ''
        else:
            return F"Hello {data}"
