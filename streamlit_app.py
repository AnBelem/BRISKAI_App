import streamlit as st


#Titulo

import streamlit as st
from PIL import Image


#img = Image.open("BRISKAI.jpg")

# display image using streamlit
# width is used to set the width of an image
#st.image(img, width=200)

# Configuración de la página
#st.set_page_config(page_title="BRISK.AI", layout="wide")

# Función de inicio de sesión
def login():
    st.set_page_config(page_title="BRISK.AI", layout="wide")
    st.title("Inicio de Sesión")
    st.write("Por favor, introduce tus datos para acceder a la aplicación.")

    # Inputs de usuario y contraseña
    username = st.text_input("Usuario:")
    password = st.text_input("Contraseña:", type="password")

    # Credenciales de ejemplo
    valid_credentials = {"admin": "12345", "user": "password123"}

    if st.button("Iniciar Sesión"):
        if username in valid_credentials and password == valid_credentials[username]:
            st.session_state["authenticated"] = True
            st.session_state["show_instructions"] = True  # Estado inicial para mostrar instrucciones
            st.session_state["user"] = username  # Guardar el usuario actual
            st.success("Inicio de sesión exitoso. Cargando las instrucciones...")
        else:
            st.error("Usuario o contraseña incorrectos.")

# Pantalla de instrucciones
def instructions():
    st.title("Cómo funciona la aplicación")
    st.write("""
    Bienvenido a **BRISK.AI**. Aquí hay una breve guía para usar la aplicación:
    s
    1. **Selecciona un segmento predeterminado o introduce un PMID:** Proporciona el PMID el cúal quieres obtener resúmen o elige uno de los segmentos predefinidos.
    2. **Configura los parámetros:** Ajusta las opciones como tokens máximos, temperatura, y el estilo del resumen (persona, idioma).
    3. **Haz clic en "Resumir":** Obtén tu texto simplificado y resumido basado en tus configuraciones.
    
    Una vez que hayas leído esto, haz clic en el botón de abajo para continuar a la aplicación principal.
    """)

    # Botón para continuar a la pantalla principal
    if st.button("Ir a la Aplicación Principal"):
        st.session_state["show_instructions"] = False

# Pantalla principal
def main_app():
    st.sidebar.button("Cerrar Sesión", on_click=lambda: st.session_state.update({"authenticated": False, "show_instructions": False, "user": None}))
    st.title("BRISK.AI")
    st.subheader(f"Bienvenido a la aplicación, {st.session_state['user']}.")
    st.write("Biomedical :blue[text summarisation] and :blue[simplification] using GPT-3.5.")

# Manejo del flujo de la aplicación
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if "show_instructions" not in st.session_state:
    st.session_state["show_instructions"] = False

# Control de navegación
if not st.session_state["authenticated"]:
    login()
elif st.session_state["show_instructions"]:
    instructions()
else:
    main_app()   

# Título principal
#st.title("BRISK.AI")
#st.write(
#    "Biomedical :blue[text summarisation] and :blue[simplification] using GPT-3.5"
#)

#st.image("Images/Red_AE_mRNA.png", caption="Imagen subida desde GitHub", use_container_width=True)
col1, col2 = st.columns([2, 2])


#st.title("BRISK.AI")
#st.write(
#    "Biomedical :blue[text summarisation] and :blue[simplification] using GPT-3.5"
#)
# Sección de entrada de texto

with col1:
    st.subheader("Selecciona un segmento predefinido:")
    selected_option = st.selectbox("Elige una opción", ["Ninguna opción seleccionada", "Ivermectina", "HCQ"])
    
    st.text_input("O introduce un PMID (Identificador Único de PubMed):")
    st.subheader("Configuración de Resumen")
    max_tokens = st.slider("Máximo número de tokens:", 200, 1000, 500, help="GPT no permite generar respuestas de cierta longitud, sino que finalizará cuando haya terminado una idea. Este valor simplemente cortará la generación para evitar incurrir en costos elevados.")
    temperature = st.slider("Temperatura:", 0.0, 1.0, 0.2, step=0.01, help="La temperatura indica qué tan reproducibles serán los resultados de GPT-3.5, donde 0 significa muy reproducible y 1 significa prácticamente aleatorio.")

    st.selectbox("¿Cómo deseas que se explique el texto?", [ "🧑 Adolescente", "👩‍💼 Adulto", "🧑‍⚕️ Clínico profesional"], index=1)
    
    comparison_mode = st.checkbox(" Mostrar comparación de resultados")

    st.selectbox("¿En qué idioma deseas el resultado?", ["EN", "DE", "FR", "IT", "ES", "JP"], index=0)

with col2:
   st.subheader("Introduce un texto para resumir:")
   input_text = st.text_area("Texto", height=200)
   
   # Botón de acción
   if st.button("¡Resumir!"):
    if not input_text:
        st.error("Por favor, introduce un texto o selecciona una opción.")
    else:
        st.success("Resumen generado con éxito.")
        st.write("Aquí aparecerá tu resumen.")  # Puedes reemplazar esto con la integración de un modelo
   st.selectbox("Red", ["Ninguna opción seleccionada", "Efectos Adversos en  vacuna mRNA", "Variante en  vacuna mRNA", "Comorbilidades en  vacuna mRNA", "Embarazo en  vacuna mRNA", "Características del virus en  vacuna mRNA", "Género en  vacuna mRNA", "Efectos Adversos en  vacuna de vector", "Variante en  vacuna de vector", "Comorbilidades en  vacuna de vector", "Embarazo en  vacuna de vector", "Características del virus en  vacuna de vector", "Género en  vacuna de vector"], index=0)

