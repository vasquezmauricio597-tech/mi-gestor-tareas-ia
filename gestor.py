import datetime
import json
import os
import requests  # La herramienta para APIs que estás estudiando

ARCHIVO_DATOS = "mis_tareas.json"

def obtener_consejo_api():
    try:
        # Hacemos una petición GET a la API (como viste en Coursera)
        respuesta = requests.get("https://api.adviceslip.com/advice")
        datos_api = respuesta.json()
        return datos_api['slip']['advice']
    except:
        return "Sigue adelante con tus objetivos."

def cargar_tareas():
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, 'r') as f:
            return json.load(f)
    return []

def guardar_tareas(lista):
    with open(ARCHIVO_DATOS, 'w') as f:
        json.dump(lista, f, indent=4)

# --- INICIO ---
mis_tareas = cargar_tareas()
print(f"--- 📝 GESTOR PRO + API (Tareas: {len(mis_tareas)}) ---")

nuevo_titulo = input("¿Qué tarea quieres agregar?: ")
es_pro = input("¿Es profesional? (si/no): ").lower() == "si"

# Llamada a la API para motivarte
consejo = obtener_consejo_api()

tarea_nueva = {
    "titulo": nuevo_titulo,
    "es_profesional": es_pro,
    "fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
    "consejo_recibido": consejo
}

mis_tareas.append(tarea_nueva)
guardar_tareas(mis_tareas)

print(f"\n✅ Guardado. Tu consejo del día (vía API):")
print(f"💡 '{consejo}'")

print("\n--- LISTA ACTUALIZADA ---")
for t in mis_tareas:
    prefijo = "⭐" if t["es_profesional"] else "☕"
    print(f"{prefijo} {t['titulo']}")