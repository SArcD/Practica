import streamlit as st
import pandas as pd
import io
import base64

# Crear un DataFrame vacío para almacenar los datos de los pacientes
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Nombre","Edad","Peso","Altura","Grasa","CMB","CMP",'FA',"Marcha"])

# Título
st.title('Ingreso de Datos de Pacientes')

# Crear un formulario para agregar datos de un paciente
with st.form('Agregar Paciente'):
    Nombre = st.text_input('Nombre del Paciente')
    Edad = st.number_input('Edad', min_value=0, max_value=120)
    Peso = st.number_input('Peso (kg)', min_value=0.0)
    Altura = st.number_input('Altura (m)', min_value=0.0)
    Grasa = st.number_input('Grasa (%)', min_value=0.0)
    CMB = st.number_input('CMB (cm)', min_value=0.0)
    CMP = st.number_input('CMP (cm)', min_value=0.0)
    FA = st.number_input('FA (kg)', min_value=0.0)
    Marcha = st.number_input('Marcha (m/s)', min_value=0.0)

    if st.form_submit_button('Agregar Paciente'):
        st.session_state.data = st.session_state.data.append({'Nombre': Nombre, 'Edad': Edad, 'Peso': Peso, 'Altura': Altura, 'Grasa': Grasa, 'CMB': CMB, 'CMP': CMP, 'FA': FA, 'Marcha': Marcha}, ignore_index=True)
        st.success('Datos del paciente agregados con éxito!')

# Ingresar el número de fila a editar
edit_row_number = st.number_input('Número de Fila a Editar', min_value=0, max_value=len(st.session_state.data)-1, value=0, step=1, key='edit_row_number')

# Crear un formulario para editar datos de un paciente
if edit_row_number is not None:
    with st.form('Editar Paciente'):
        st.subheader('Editar Fila {}'.format(edit_row_number))
        data_table = st.session_state.data.copy()
        st.dataframe(data_table, height=400, width=800)

        Nombre = st.text_input('Nombre del Paciente', value=data_table.iloc[edit_row_number]['Nombre'])
        Edad = st.number_input('Edad', min_value=0, max_value=150, value=data_table.iloc[edit_row_number]['Edad'])
        Peso = st.number_input('Peso (kg)', min_value=0.0, value=data_table.iloc[edit_row_number]['Peso'])
        Altura = st.number_input('Altura (m)', min_value=0.0, value=data_table.iloc[edit_row_number]['Altura'])
        Grasa = st.number_input('Grasa (%)', min_value=0.0, value=data_table.iloc[edit_row_number]['Grasa'])
        CMB = st.number_input('CMB (cm)', min_value=0.0, value=data_table.iloc[edit_row_number]['CMB'])
        CMP = st.number_input('CMP (cm)', min_value=0.0, value=data_table.iloc[edit_row_number]['CMP'])
        FA = st.number_input('FA (kg)', min_value=0.0, value=data_table.iloc[edit_row_number]['FA'])
        Marcha = st.number_input('Marcha (m/s)', min_value=0.0, value=data_table.iloc[edit_row_number]['Marcha'])

        if st.form_submit_button('Guardar Cambios'):
            data_table.iloc[edit_row_number] = [Nombre, Edad, Peso, Altura, Grasa, CMB, CMP, FA, Marcha]
            st.session_state.data = data_table

# Mostrar los datos ingresados en el DataFrame
if st.button('Mostrar Resultados'):
    st.subheader('DataFrame Resultante')
    st.write(st.session_state.data)

# Botón para descargar los datos en formato Excel
if not st.session_state.data.empty:
    st.subheader('Descargar Datos')
    st.write('Haga clic en el enlace a continuación para descargar los datos en formato Excel.')
    
    # Generar un enlace para la descarga del archivo Excel
    output = io.BytesIO()
    excel_writer = pd.ExcelWriter(output, engine='xlsxwriter')
    st.session_state.data.to_excel(excel_writer, sheet_name='Datos', index=False)
    excel_writer.save()
    
    # Crear el enlace de descarga
    excel_data = output.getvalue()
    b64 = base64.b64encode(excel_data).decode('utf-8')
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="datos_pacientes.xlsx">Descargar Excel</a>'
    st.markdown(href, unsafe_allow_html=True)


#####################
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math

# Cargar los datos (reemplaza esto con la carga de tus datos reales)
# df2021C = ...

# Obtener las columnas numéricas
numeric_columns = data_table.select_dtypes(include='number').columns

# Configurar el número de subplots por fila
subplots_per_row = 3

# Calcular el número de filas necesarias para todos los subplots
num_rows = math.ceil(len(numeric_columns) / subplots_per_row)

# Título
st.title('Histogramas de Parámetros')

# Ajuste del número de bins
num_bins = st.slider('Número de Bins', min_value=1, max_value=50, value=10)

# Crear subplots
fig = make_subplots(rows=num_rows, cols=subplots_per_row, subplot_titles=numeric_columns)

# Graficar los histogramas
for i, column in enumerate(numeric_columns):
    row = i // subplots_per_row + 1
    col = i % subplots_per_row + 1
    fig.add_trace(go.Histogram(x=data_table[column], nbinsx=num_bins, name=column, marker=dict(line=dict(color='black', width=1))), row=row, col=col)

# Actualizar el diseño de los subplots
fig.update_layout(showlegend=False, height=400*num_rows, width=800, title_text='Histogramas de Parámetros')

# Mostrar los subplots en Streamlit
st.plotly_chart(fig)

################## Diagrama de caja #####

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def create_boxplot_subplot(df, column):
    fig = px.box(df, y=column)
    return fig

st.title('Diagramas de Caja')

# Crear un DataFrame de ejemplo
#data = {
#    'Edad': np.random.randint(20, 60, 50),
#    'Peso': np.random.randint(50, 100, 50),
#    'Altura': np.random.uniform(1.5, 2.0, 50),
#    'Grasa': np.random.randint(10, 30, 50),
#    'CMB': np.random.randint(80, 110, 50),
#    'CMP': np.random.randint(90, 120, 50),
#    'FA': np.random.randint(40, 70, 50),
#    'Marcha': np.random.uniform(0.8, 1.5, 50)
#}

#data_table = pd.DataFrame(data)

numeric_columns = data_table.select_dtypes(include=['number']).columns

num_cols = 2  # Número de columnas en la cuadrícula

num_rows = len(numeric_columns) // num_cols + (len(numeric_columns) % num_cols > 0)

for i in range(num_rows):
    cols = st.columns(num_cols)
    for j in range(num_cols):
        idx = i * num_cols + j
        if idx < len(numeric_columns):
            with cols[j]:
                column = numeric_columns[idx]
                st.subheader(f'Diagrama de Caja para {column}')
                fig = create_boxplot_subplot(data_table, column)
                st.plotly_chart(fig, use_container_width=True)


#######################

import streamlit as st

# Crear las pestañas
tabs = st.tabs(["Pestaña 1", "Pestaña 2", "Pestaña 3"])

# Contenido de la pestaña 1
with tabs[0]:
    st.title("Contenido de la Pestaña 1")
    st.write("¡Bienvenido a la Pestaña 1!")

# Contenido de la pestaña 2
with tabs[1]:
    st.title("Contenido de la Pestaña 2")
    st.write("¡Estás en la Pestaña 2 ahora!")

# Contenido de la pestaña 3
with tabs[2]:
    st.title("Contenido de la Pestaña 3")
    st.write("Explora la Pestaña 3 aquí.")
En este ejemplo, estamos utilizando la función st.tabs() para crear las pestañas y luego estamos utilizando bloques with para definir el contenido de cada pestaña. Cada bloque with tabs[i]: contiene el contenido específico que deseas mostrar en esa pestaña. Puedes personalizar el contenido de cada pestaña con texto, gráficos, widgets interactivos y más.

Recuerda que necesitarás tener Streamlit instalado en tu entorno para poder ejecutar este código. Puedes instalarlo utilizando el siguiente comando:

Copy code
pip install streamlit
Una vez que tengas Streamlit instalado, puedes ejecutar el script y abrirá automáticamente una página web con las pestañas que has creado.








