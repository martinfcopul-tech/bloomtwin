# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- CONFIG ----------
st.set_page_config(page_title="BloomTwin", layout="wide")
st.title("🌸 BloomTwin – Pasado, Presente y Futuro de la Floración")

# ---------- CARGA DATOS ----------
# Subir el CSV al repo y referenciarlo por nombre
df = pd.read_csv("bloom_full.csv")

# ---------- GRÁFICA INTERACTIVA ----------
fig = px.line(df, x='year', y='meanNDVI',
              title='NDVI máximo anual (1984-2026)',
              markers=True, height=350)
fig.update_layout(hovermode='x unified',
                  xaxis_title='Año',
                  yaxis_title='NDVI (0-1)',
                  font=dict(size=14),
                  template='plotly_white')

# ---------- LAYOUT ----------
left, right = st.columns([2, 1])

with left:
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("¿Qué ver?")
    st.write("- **1984-2023**: datos Landsat reales")
    st.write("- **2024-2026**: predicción LSTM")
    st.markdown("**Valor alto ≈ mayor floración**")

# ---------- TABLA OPCIONAL ----------
with st.expander("Ver tabla"):
    st.dataframe(df)

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Datos procesados con Google Earth Engine – Modelo LSTM en TensorFlow")