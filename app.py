import streamlit as st
import datetime
import json
import os
import requests

ARCHIVO_DATOS = "mis_tareas.json"

# Funciones de soporte
def cargar_tareas():
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, 'r') as f:
            return json.load(f)
    return []

def guardar_tareas(lista):
    with open(ARCHIVO_DATOS, 'w') as f:
        json.dump(lista, f, indent=4)

def obtener_consejo():
    try:
        r = requests.get("https://api.adviceslip.com/advice")
        return r.json()['slip']['advice']
    except:
        return "Keep pushing forward!"

# --- INTERFAZ DE STREAMLIT ---
st.set_page_config(page_title="Mi Gestor IA", page_icon="🧠")
st.title("🚀 Mi Gestor de Tareas Personal")

# Cargar datos
if 'tareas' not in st.session_state:
    st.session_state.tareas = cargar_tareas()

# Formulario para nueva tarea
with st.form("nueva_tarea"):
    titulo = st.text_input("¿Qué tienes pendiente?")
    es_pro = st.checkbox("¿Es una tarea profesional/académica?")
    submit = st.form_submit_button("Agregar Tarea")

if submit and titulo:
    consejo = obtener_consejo()
    nueva = {
        "titulo": titulo,
        "es_profesional": es_pro,
        "fecha": datetime.datetime.now().strftime('%d/%m/%Y'),
        "consejo": consejo
    }
    st.session_state.tareas.append(nueva)
    guardar_tareas(st.session_state.tareas)
    st.success(f"¡Tarea guardada! Consejo: {consejo}")

# Mostrar tareas de forma visual
st.subheader("Tus tareas actuales")
for i, t in enumerate(st.session_state.tareas):
    with st.expander(f"{'⭐' if t['es_profesional'] else '☕'} {t['titulo']}"):
        st.write(f"📅 Creada el: {t['fecha']}")
        st.info(f"💡 Consejo de la API: {t.get('consejo', 'No hay consejo disponible')}")