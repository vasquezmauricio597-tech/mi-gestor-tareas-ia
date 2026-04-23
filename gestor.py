import datetime  # Importamos la herramienta de tiempo

# 1. Datos de la tarea (Abstracción)
titulo = "Estudiar Python para Data Science" # Puedes cambiar esto por tu curso de IBM [cite: 6]
es_profesional = True
estado = "En progreso"
# Guardamos el momento exacto en que se crea la tarea
timestamp_creacion = datetime.datetime.now() 

# 2. Lógica de clasificación y color
if es_profesional:
    color = "CLARO (Amarillo)"
    posicion = "INICIO"
else:
    color = "OSCURO (Gris)"
    posicion = "FINAL"

# 3. Mostrar resultados
print(f"--- GESTOR DE TAREAS ---")
print(f"Tarea: {titulo}")
print(f"Posición: {posicion} | Color: {color}")
print(f"Creada el: {timestamp_creacion.strftime('%d/%m/%Y %H:%M')}")