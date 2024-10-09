import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import altair as alt
import time
import zipfile

# Page title
st.set_page_config(page_title='ML model builder', page_icon='🏗️')
st.title('🏗️ Pagina para pruebas de Streamlit')


import streamlit as st

# Inicializar valores en session_state si no existen
if 'contador' not in st.session_state:
    st.session_state.contador = 0

# Mostrar el valor actual
st.write(f"Valor del contador: {st.session_state.contador}")

# Botón para incrementar el contador
if st.button('Incrementar'):
    st.session_state.contador += 1


