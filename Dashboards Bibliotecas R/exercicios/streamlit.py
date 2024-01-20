import pandas as pd
import streamlit as st
import numpy as np

st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")

locais = st.selectbox('Escolha um local', ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'])


# crie um mapa de fortaleza com as coordenadas -3.7172, -38.5433

