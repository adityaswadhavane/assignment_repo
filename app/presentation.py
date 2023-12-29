import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title('ABC-XYZ Analysis Assignment')

data = pd.read_excel('../data/presentation/results.xlsx')
def fig1_pareto_chart(data):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    result = data.sort_values(by='total_price_sum',ascending=False)

    fig.add_trace(go.Bar(x=result['product_code'], 
        y=result['total_price_sum'], name='total_inventory_sum'),
        secondary_y=False,
    )

    fig.add_trace(go.Scatter(x=result['product_code'], 
        y=result['cumulative_percentage'], name='cumulative_percentage'),
        secondary_y=True,
    )
    return fig


def fig2_distribution_abc_category(data):
    results =data['ABC_category'].value_counts().reset_index()
    fig = px.pie(
        names=results['ABC_category'].unique(),
        values=results['count'],
        title='Pie Chart for Distribution of ABC Category',
        hole=0.3
    )
    return fig

def fig3(result):
    fig = px.histogram(
            x=result['product_code']
            ,y=result['total_inventory_sum']
            ,color=result['ABC_category']
        )
    fig.update_xaxes(title_text="Product Code")
    fig.update_yaxes(title_text="Total Inventory Sum")
    return fig

cols = st.empty()

charts = {'Pareto Chart':fig1_pareto_chart(data),
'Percentage Distribution of ABC category':fig2_distribution_abc_category(data),
'Distribution of ABC Catrgory by inventory':fig3(data)}
with st.sidebar:
    st.markdown("## Here are Some Charts of Analysis")
    select_chart = st.selectbox("Select from drop-down",list(charts.keys()))
    cols.plotly_chart(charts[select_chart])