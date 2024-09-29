import streamlit as st
import pandas as pd
import plotly as df
import json


file = open('vendas.json')
data = json.load(file)
# print(data)

df = pd.DataFrame.from_dict(data)

# print(df)

file.close()