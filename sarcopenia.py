import streamlit as st
import pandas as pd
import io
import base64


import streamlit as st

# Opciones de pestañas en el panel lateral
tabs = ["Inicio", "todo de sorcopenia", "Ayuda"]
selected_tab = st.sidebar.radio("Selecciona una pestaña", tabs)

# Mostrar contenido basado en la pestaña seleccionada
if selected_tab == "Inicio":
    st.title("Base de datos de acusmulos")
    st.write("¿Cómo usarlo? Se introducen los tatos en la table y al final se despliegan diagramas de caja analizando los resultados de toda la base de datos.")

elif selected_tab == "todo de sorcopenia":
    st.title("todo de sorcopenia")
    st.write("Ajusta la configuración aquí.")

st.write("# Sobre envejecimiento y la sarcopenia :older_adult: :older_woman:")


"""La sarcopenia es un término médico utilizado para describir la pérdida gradual y progresiva de masa muscular y fuerza que ocurre con el envejecimiento. Es un fenómeno común en las personas mayores, y puede tener efectos significativos en la salud y la calidad de vida. La sarcopenia puede afectar la capacidad funcional, la independencia y la movilidad de las personas mayores, aumentando el riesgo de caídas, fracturas y otras complicaciones.

La pérdida de masa muscular asociada con la sarcopenia se debe a una combinación de factores, incluyendo cambios hormonales, disminución de la actividad física, disminución de la ingesta de proteínas y otros factores metabólicos. La sarcopenia no solo afecta a los músculos esqueléticos, sino también a otros tejidos musculares, como el corazón.

Es importante destacar que la sarcopenia no es simplemente una parte inevitable del envejecimiento, y se pueden tomar medidas para prevenirla o retrasar su progresión. Estas medidas incluyen mantener un estilo de vida activo y saludable, realizar ejercicios de resistencia para mantener y aumentar la masa muscular, y asegurarse de tener una ingesta adecuada de proteínas y nutrientes esenciales.

La evaluación y el diagnóstico de la sarcopenia pueden involucrar medidas como la medición de la masa muscular, la fuerza muscular y la función física. Los profesionales de la salud pueden utilizar diferentes criterios y pruebas para determinar si una persona tiene sarcopenia y si es necesario intervenir con cambios en el estilo de vida o tratamientos específicos."""



tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Fuerza de brazo", "Circunferencia de Pantorrilla", "Velocidad de Marcha","Perimetro de Brazo","Porcentaje de grasa","Masa musculo-esquelética","grasa"])

with tab1:
    st.header("Fuerza de brazo")
    st.markdown(
        """
        Se mide la fuerza de presion del paciente utilizando un :blue[dinamómetro]. La prueba se realiza 
        en el brazo dominante, flexionado a 90 grados, con el paciente sentado en una silla. La unidad de medida son los kilogramos. 
        Esta prueba permite establecer puntos de corte para fragilidad, dependiendo del indice de masa corporal del paciente. 
        En Hombres estos son menos de 29 kg (IMC<24), 30 kg (IMC[24,28]) y 32 kg (IMC > 28). En la mujeres los puntos de corte son: 
        menor a 17 kg (IMC < 23), menor a 17.3 kg (IMC [23.1,26]), menor a 18 kg (IMC [26,29]) y menor a 21 kg (IMC > 29).
        """
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        # Carga y muestra una imagen con ancho y alto específicos
        #image = "https://raw.githubusercontent.com/SantiagoArceoDiaz/AMDatabase/547b9d1f27ac2e5c5396f35cc85507e74b92404f/pages/Dina.png"
        #width = 600  # Ancho deseado en píxeles
        # Mostrar la imagen centrada
        #caption=st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
        #st.image(image) #caption=':blue [Medición de la fuerza usando un dinamómetro digital]', width=width)
        #st.caption(' :blue[Medición de la fuerza de agarre usando un dinamómetro digital]')
        #st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
        st.write(" ")
    with col2:
        # Carga y muestra una imagen con ancho y alto específicos
        # image = "https://raw.githubusercontent.com/SantiagoArceoDiaz/AMDatabase/547b9d1f27ac2e5c5396f35cc85507e74b92404f/pages/Dina.png"
        image = 'Calf.jpeg'
        width = 600  # Ancho deseado en píxeles
        # Mostrar la imagen centrada
        #caption=st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
        st.image(image) #caption=':blue [Medición de la fuerza usando un dinamómetro digital]', width=width)
        st.caption(' :blue[Medición de la fuerza de agarre usando un dinamómetro digital]')
        #st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

    
    with col3:
        st.write(' ')



with tab2:
    st.header("Circunferencia de Pantorrilla")
    st.markdown(
    """La prueba de circunferencia de pantorrilla es una medida clínica utilizada para evaluar la masa muscular periférica en adultos mayores. Esta prueba es una evaluación simple y no invasiva de la masa muscular que se puede realizar en un entorno clínico o en el hogar. La circunferencia de la pantorrilla es un indicador útil de la masa muscular periférica debido a la alta correlación entre la circunferencia de la pantorrilla y la masa muscular total. La disminución de la masa muscular periférica es un indicador común de la disminución de la fuerza y ​​la función muscular en adultos mayores, lo que se asocia con una mayor discapacidad, caídas y mortalidad. Para realizar la prueba de circunferencia de pantorrilla, se mide la circunferencia de la pantorrilla desnuda en la pierna dominante, en un punto específico, generalmente en la parte más ancha de la pantorrilla. La medida se toma utilizando una cinta métrica flexible y se registra en centímetros. Los valores normales de la circunferencia de la pantorrilla pueden variar según la edad, el sexo y la etnia, pero generalmente se considera normal una medida superior a 31 cm en mujeres y 34 cm en hombres. La prueba de circunferencia de pantorrilla es una herramienta útil para la evaluación de la masa muscular periférica en adultos mayores, pero debe usarse junto con otras medidas clínicas y pruebas de función muscular para una evaluación más completa del estado de la masa muscular y la fuerza en los adultos mayores.
    """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        # Carga y muestra una imagen con ancho y alto específicos
        image = 'https://raw.githubusercontent.com/SantiagoArceoDiaz/AMDatabase/main/pages/Calf.jpeg'
        width = 600  # Ancho deseado en píxeles
        # Mostrar la imagen centrada
        #caption=st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
        st.image(image) #caption=':blue [Medición de la fuerza usando un dinamómetro digital]', width=width)
        st.caption(' :blue[Medición de la circunferencia de pantorrilla]')
        #st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')    
    with col3:
        st.write(' ')





with tab3:
    st.header("Velocidad de Marcha")
    st.markdown(
    """ La prueba de velocidad de marcha, también conocida como prueba de la marcha de 4 metros, es una evaluación simple y rápida que se utiliza comúnmente en adultos mayores para medir su velocidad de marcha y su capacidad funcional. La prueba implica cronometrar el tiempo que tarda una persona en caminar cuatro metros a su ritmo habitual. La velocidad de marcha se considera un predictor importante de la capacidad funcional de los adultos mayores, lo que significa que puede ser un indicador de su capacidad para realizar actividades diarias y su calidad de vida en general. En particular, se ha demostrado que la velocidad de marcha se correlaciona con la capacidad para realizar actividades básicas de la vida diaria, como levantarse de una silla, caminar y subir escaleras, así como con la capacidad para realizar actividades instrumentales de la vida diaria, como hacer compras, cocinar y manejar el dinero. Además de ser una herramienta útil para la evaluación de la capacidad funcional, la prueba de velocidad de marcha también se ha utilizado como predictor de la mortalidad en adultos mayores. Se ha demostrado que una velocidad de marcha lenta se asocia con un mayor riesgo de mortalidad en esta población. En resumen, la prueba de velocidad de marcha es una herramienta importante para la evaluación de la capacidad funcional y la salud en adultos mayores. Permite a los profesionales de la salud identificar a las personas que pueden estar en mayor riesgo de limitaciones funcionales y desarrollar planes de tratamiento y prevención para mejorar su calidad de vida y reducir su riesgo de mortalidad.
    """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        # Carga y muestra una imagen con ancho y alto específicos
        image = 'https://raw.githubusercontent.com/SantiagoArceoDiaz/AMDatabase/main/pages/VelMarch.PNG'
        width = 600  # Ancho deseado en píxeles
        # Mostrar la imagen centrada
        #caption=st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
        st.image(image) #caption=':blue [Medición de la fuerza usando un dinamómetro digital]', width=width)
        st.caption(' :blue[Prueba de velocidad de marcha de 4 metros]')
        #st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')    
    with col3:
        st.write(' ')


with tab4:
    
    st.header("Circunferencia de brazo")
    st.markdown(
    """ 
    
    El perímetro del brazo se mide como la circunferencia alrededor del brazo, generalmente en la mitad superior del brazo. Para medir el perímetro del brazo, se utiliza una cinta métrica flexible y no elástica. El individuo debe estar de pie o sentado con el brazo relajado y extendido a lo largo del cuerpo. La cinta métrica se coloca alrededor del brazo en el punto medio entre el hombro y el codo, asegurándose de que esté nivelada y ajustada sin apretar demasiado la piel. La medición se toma en centímetros o pulgadas, y se registra como la circunferencia del brazo.

    La relación entre el perímetro del brazo y la sarcopenia se basa en la idea de que el perímetro del brazo puede ser un indicador indirecto de la masa muscular en esa región del cuerpo. Un brazo más delgado podría estar relacionado con una disminución de la masa muscular, lo que podría ser un signo de sarcopenia. Sin embargo, es importante tener en cuenta que el perímetro del brazo por sí solo no proporciona una imagen completa de la salud muscular y no es un diagnóstico definitivo de sarcopenia.

    El perímetro del brazo a menudo se utiliza en combinación con otras medidas, como la medición de la masa muscular y la fuerza, para evaluar el estado de la sarcopenia. Los profesionales de la salud pueden utilizar herramientas de evaluación más completas, como la medición de la masa muscular esquelética mediante DEXA, análisis de impedancia bioeléctrica y pruebas de función muscular, para obtener una imagen más precisa de la salud muscular y diagnosticar la sarcopenia.

    En resumen, el perímetro del brazo puede ser una medida simple y rápida para evaluar posibles signos de pérdida de masa muscular, pero se utiliza mejor en conjunto con otras medidas y pruebas más completas para evaluar y diagnosticar la sarcopenia de manera precisa. Si tienes preocupaciones sobre la sarcopenia, es importante hablar con un profesional de la salud para una evaluación completa y adecuada.
    """
    )
 
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        # Carga y muestra una imagen con ancho y alto específicos
        image = 'Arm-circumference.jpg'
        width = 600  # Ancho deseado en píxeles
        # Mostrar la imagen centrada
        #caption=st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
        st.image(image) #caption=':blue [Medición de la fuerza usando un dinamómetro digital]', width=width)
        st.caption(' :blue[Medición de la circunferencia de brazo](https://www.youtube.com/watch?v=zJZGW-TD23E)')    
    with col3:
        st.write(' ')




with tab5:
    
    st.header("Porcentaje de Grasa")
    st.markdown(
    """ 
    El porcentaje de grasa corporal se mide utilizando una variedad de métodos, que van desde técnicas más simples hasta métodos más avanzados y precisos. Algunas de las formas comunes de medir el porcentaje de grasa corporal incluyen:

    - Caliper de Pliegue Cutáneo: Este método implica medir el grosor de los pliegues cutáneos en diferentes áreas del cuerpo con un calibrador. Estas mediciones se utilizan para estimar el grosor total de la grasa subcutánea y calcular el porcentaje de grasa corporal.

    - Bioimpedancia: Al igual que para medir la masa muscular esquelética, la bioimpedancia se puede utilizar para medir el porcentaje de grasa corporal. Este método mide la resistencia eléctrica del cuerpo al paso de una corriente eléctrica de bajo nivel y utiliza esta información para estimar la cantidad de tejido graso.

    - Densitometría de Doble Energía de Rayos X (DXA o DEXA): Además de medir la masa muscular esquelética, la DXA también puede proporcionar información sobre la grasa corporal. Esta técnica utiliza rayos X de dos energías diferentes para medir la densidad de los tejidos y calcular el porcentaje de grasa corporal.

    - Tomografía Computarizada (TC) y Resonancia Magnética (RM): Al igual que para medir la masa muscular esquelética, la TC y la RM también se pueden utilizar para obtener imágenes detalladas de los tejidos grasos y calcular el porcentaje de grasa corporal.

    - Métodos de Impedancia de Aire: Estos métodos utilizan mediciones de la masa y el volumen corporal junto con la densidad del cuerpo para estimar la grasa corporal.

    La relación entre el porcentaje de grasa corporal y la sarcopenia es importante debido a su interacción en la composición corporal general. La sarcopenia se caracteriza por la pérdida de masa muscular esquelética, mientras que el aumento del porcentaje de grasa corporal puede llevar a un exceso de peso y obesidad. La sarcopenia y la obesidad a menudo se denominan "obesidad sarcopénica" cuando ocurren juntas.

    La obesidad sarcopénica es una combinación de estas dos condiciones, donde una persona tiene un alto porcentaje de grasa corporal junto con una disminución de la masa muscular. Esto puede ser especialmente perjudicial, ya que la pérdida de masa muscular contribuye a una disminución de la fuerza y la funcionalidad, lo que puede aumentar el riesgo de discapacidad y otros problemas de salud. Además, la obesidad sarcopénica también se ha asociado con un mayor riesgo de enfermedades crónicas como la diabetes tipo 2, enfermedades cardíacas y problemas metabólicos.

    Es importante tener en cuenta que la relación entre el porcentaje de grasa corporal y la sarcopenia puede ser compleja y variar según la situación individual. Una evaluación completa de la composición corporal y la función muscular es crucial para comprender cómo estas dos condiciones pueden interactuar y afectar la salud general de una persona.
    """
    )
    image = 'https://github.com/SantiagoArceoDiaz/AMDatabase/blob/main/fat-content.jpeg'
    st.image(image, caption="Prueba de velocidad de marcha de 4 metros")
    st.write( "Prueba de velocidad de marcha](https://www.youtube.com/watch?v=zJZGW-TD23E)")

with tab6:

    st.header("Masa musculo-esquelética")
    st.markdown(
    """
    El porcentaje de masa muscular esquelética se mide utilizando técnicas de imagenología y mediciones antropométricas. Algunos de los métodos más comunes para medir la masa muscular esquelética incluyen:

    - Densitometría de Doble Energía de Rayos X (DXA o DEXA): Esta técnica se utiliza comúnmente para medir la densidad mineral ósea, pero también puede proporcionar información sobre la masa muscular magra. DXA utiliza rayos X de dos energías diferentes para medir la cantidad de tejido magro en el cuerpo.

    - Tomografía Computarizada (TC): La TC puede utilizarse para obtener imágenes detalladas de los músculos y medir su volumen y densidad. A partir de esta información, se puede calcular el porcentaje de masa muscular esquelética.

    - Resonancia Magnética (RM): Al igual que la TC, la RM puede proporcionar imágenes detalladas de los tejidos musculares, lo que permite calcular el volumen y la masa muscular magra.

    - Bioimpedancia: Este método mide la resistencia eléctrica del cuerpo al paso de una corriente eléctrica de bajo nivel. La resistencia está relacionada con la cantidad de tejido magro, incluida la masa muscular.

    - Mediciones antropométricas: Estas incluyen la medición de circunferencias de brazos, piernas y otros segmentos del cuerpo, así como la medición de pliegues cutáneos. Si bien estas medidas pueden proporcionar una estimación del contenido de grasa y masa muscular, son menos precisas que las técnicas de imagen avanzadas.

    La relación entre el porcentaje de masa muscular esquelética y la sarcopenia es directa. La sarcopenia se caracteriza por una disminución significativa de la masa muscular esquelética, lo que conduce a la pérdida de fuerza muscular y funcionalidad. A medida que disminuye la masa muscular, las personas pueden experimentar una disminución en su capacidad para realizar actividades diarias, lo que a su vez puede aumentar el riesgo de caídas, fracturas y discapacidad.

    La medición del porcentaje de masa muscular esquelética es importante en la evaluación y diagnóstico de la sarcopenia. La disminución de la masa muscular es un marcador clave de la enfermedad y se utiliza para identificar a las personas en riesgo de desarrollar sarcopenia. Los profesionales de la salud pueden utilizar estas mediciones junto con otras evaluaciones clínicas y funcionales para determinar si una persona tiene sarcopenia y desarrollar un plan de tratamiento adecuado, que puede incluir ejercicio, cambios en la dieta y otras intervenciones.
    """
    )

with tab7:
    st.header("otro nombre")
    st.markdown("oihfdiouhgodfhiosfhsiodfhsiofhiosf")
    col1, col2, col3 = st.columns(3)
    with col1:
        # Carga y muestra una imagen con ancho y alto específicos
        image = "https://raw.githubusercontent.com/SantiagoArceoDiaz/AMDatabase/547b9d1f27ac2e5c5396f35cc85507e74b92404f/pages/Dina.png"
        width = 600  # Ancho deseado en píxeles
        # Mostrar la imagen centrada
        caption=st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
        st.image(image) #caption=':blue [Medición de la fuerza usando un dinamómetro digital]', width=width)
        st.caption(' :blue[Medición de la fuerza de agarre usando un dinamómetro digital]')
        st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
        st.write(" ")
    with col2:
        # Carga y muestra una imagen con ancho y alto específicos
        # image = "https://raw.githubusercontent.com/SantiagoArceoDiaz/AMDatabase/547b9d1f27ac2e5c5396f35cc85507e74b92404f/pages/Dina.png"
        image = 'Calf.jpeg'
        width = 600  # Ancho deseado en píxeles
        # Mostrar la imagen centrada
        #caption=st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
        st.image(image) #caption=':blue [Medición de la fuerza usando un dinamómetro digital]', width=width)
        st.caption(' :blue[Medición de la fuerza de agarre usando un dinamómetro digital]')
        #st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

    
    with col3:
        st.write(' ')

#######################################


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
# En este ejemplo, estamos utilizando la función st.tabs() para crear las pestañas y luego estamos utilizando bloques with para definir el contenido de cada pestaña. Cada bloque with tabs[i]: contiene el contenido específico que deseas mostrar en esa pestaña. Puedes personalizar el contenido de cada pestaña con texto, gráficos, widgets interactivos y más.

# Recuerda que necesitarás tener Streamlit instalado en tu entorno para poder ejecutar este código. Puedes instalarlo utilizando el siguiente comando:




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



