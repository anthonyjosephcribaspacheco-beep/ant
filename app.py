import streamlit as st
import random

# CONFIGURACIÓN
st.set_page_config(page_title="Detector de Precio Fiesta", page_icon="🎉")

# 🎨 FONDO BONITO
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

h1, h2, h3, p, label {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# TÍTULO
st.title("🛍️ ¿Es barato o caro?")
st.markdown("Desliza la barra para elegir el precio del producto:")

# 🎚️ SLIDER
precio = st.slider("Precio (€)", 0, 500, 50)

# PRECIO DE REFERENCIA
precio_referencia = 100

# MENSAJE DINÁMICO AUTOMÁTICO
if precio < precio_referencia:
    st.success(f"🎉 ¡Es BARATO! Aprovecha la oferta, solo cuesta {precio} €")
elif precio == precio_referencia:
    st.info(f"🤔 Precio normal, {precio} € es estándar en el mercado")
else:
    st.error(f"💸 Es CARO, {precio} € puede ser demasiado alto")
    st.markdown("😢 😢 😢 😢 😢 😢 😢")

# BOTÓN PARA EFECTOS DE FIESTA
if st.button("Comprobar precio"):

    st.divider()

    st.metric("Precio seleccionado:", f"{precio} €")

    if precio < precio_referencia:
        st.balloons()
        st.snow()  # efecto extra divertido
