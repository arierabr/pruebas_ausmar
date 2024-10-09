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

tabla = pd.read_csv("data/tabla_st_01.csv", encoding='utf-8')


preguntas_template = [
    "¿Cuantos origenes distintos tenemos?",     # 0
    "¿Cuál es el {ordinal} origen?",            # 1
    "¿Cuántas personas parten de este punto?",  # 2
    "¿Fecha de salida?",                        # 3
    "¿Momento de salida?",                      # 4
    "¿Fecha de llegada?",                       # 5
    "¿Momento de llegada?"]                     # 6


# Inicializar el estado de la pregunta actual si no existe
if 'indice' not in st.session_state:
    st.session_state.indice = 0

# Inicializar el número de origen actual si no existe
if 'origen_actual' not in st.session_state:
    st.session_state.origen_actual = ''

# Inicializar el número de orígenes si no existe
if 'total_origenes' not in st.session_state:
    st.session_state.total_origenes = None  # Cambiado a None para control de flujo

# Inicializar un diccionario para almacenar las respuestas si no existe
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}

# Inicializar la respuesta del usuario
if 'input' not in st.session_state:
    st.session_state.input = ""



origen = st.selectbox("Selecciones el origen", tabla.Airport)



import streamlit as st

# Inicializar valores en session_state si no existen
if 'contador' not in st.session_state:
    st.session_state.contador = 0

# Mostrar el valor actual
st.write(f"Valor del contador: {st.session_state.contador}")

# Botón para incrementar el contador
if st.button('Incrementar'):
    st.session_state.contador += 1

if 'contador' not in st.session_state or st.button('Resetear contador'):
    st.session_state.contador = 0


# Inicializar la lista de tareas si no está creada
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []

# Agregar un nuevo elemento
new_task = st.text_input("Nueva tarea")

if st.button("Agregar tarea"):
    if new_task:
        st.session_state.todo_list.append(new_task)


# Mostrar la lista de tareas actual
st.write("Tareas actuales:")
for task in st.session_state.todo_list:
    st.write(f"- {task}")

# Opción para borrar todas las tareas
if st.button("Borrar todas las tareas"):
    st.session_state.todo_list.clear()
