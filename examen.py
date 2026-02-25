import streamlit as st

# ===============================
# 1️⃣ BANCO DE PREGUNTAS
# ===============================

preguntas = [
    {"texto": "¿Cuál es el planeta más grande del Sistema Solar?", 
     "opciones": ["Marte", "Saturno", "Júpiter", "Venus"], 
     "correcta": "Júpiter"},

    {"texto": "¿En qué año se hundió el Titanic?", 
     "opciones": ["1912", "1905", "1920", "1898"], 
     "correcta": "1912"},

    {"texto": "¿Quién pintó 'La última cena'?", 
     "opciones": ["Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Dalí"], 
     "correcta": "Leonardo da Vinci"},

    {"texto": "¿Cuál es el elemento químico con el símbolo 'Au'?", 
     "opciones": ["Plata", "Cobre", "Oro", "Aluminio"], 
     "correcta": "Oro"},

    {"texto": "¿Qué país tiene forma de bota?", 
     "opciones": ["Grecia", "España", "Italia", "Portugal"], 
     "correcta": "Italia"},

    {"texto": "¿Cuántos corazones tiene un pulpo?", 
     "opciones": ["1", "2", "3", "4"], 
     "correcta": "3"},

    {"texto": "¿Cuál es la capital de Japón?", 
     "opciones": ["Kioto", "Osaka", "Tokio", "Hiroshima"], 
     "correcta": "Tokio"},

    {"texto": "¿Qué animal es el símbolo de la paz?", 
     "opciones": ["Águila", "Paloma", "Colibrí", "Cisne"], 
     "correcta": "Paloma"},

    {"texto": "¿Cuál es el río más largo del mundo?", 
     "opciones": ["Nilo", "Amazonas", "Misisipi", "Danubio"], 
     "correcta": "Amazonas"},

    {"texto": "¿En qué continente se encuentra el desierto del Sahara?", 
     "opciones": ["Asia", "América", "África", "Oceanía"], 
     "correcta": "África"}
]

# ===============================
# 2️⃣ CONFIGURACIÓN DE PÁGINA
# ===============================

st.set_page_config(page_title="Súper Quiz", page_icon="📝")
st.title("🏆 Mi Examen Interactivo")
st.write("Demuestra tus conocimientos. ¡Si sacas más de un 8 habrá sorpresa!")

# ===============================
# 3️⃣ FORMULARIO
# ===============================

with st.form("quiz_form"):
    respuestas_usuario = []

    for i, pregunta in enumerate(preguntas):
        st.subheader(f"Pregunta {i+1}: {pregunta['texto']}")
        eleccion = st.radio(
            "Elige tu respuesta:",
            pregunta["opciones"],
            key=f"p_{i}"
        )
        respuestas_usuario.append(eleccion)
        st.write("---")

    boton_enviar = st.form_submit_button("Entregar Examen")

# ===============================
# 4️⃣ CORRECCIÓN
# ===============================

if boton_enviar:
    aciertos = 0
    total = len(preguntas)

    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1

    nota = round((aciertos / total) * 10, 2)
    porcentaje = round((aciertos / total) * 100, 1)

    st.divider()
    st.header(f"📊 Nota Final: {nota} / 10")
    st.write(f"Has obtenido un {porcentaje}% de aciertos.")
    st.write(f"Aciertos: {aciertos} de {total}")

    # Mensajes según nota
    if nota >= 8:
        st.success("¡INCREÍBLE! ¡Eres un crack!")
        st.balloons()
    elif nota >= 5:
        st.warning("¡Aprobado! Buen trabajo.")
    else:
        st.error("Necesitas practicar un poco más. ¡No te rindas!")

    # Mostrar respuestas incorrectas
    st.subheader("📌 Revisión:")
    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            st.write(f"✅ Pregunta {i+1}: Correcta")
        else:
            st.write(
                f"❌ Pregunta {i+1}: Tu respuesta fue '{respuestas_usuario[i]}'. "
                f"La correcta es '{preguntas[i]['correcta']}'."
            )
