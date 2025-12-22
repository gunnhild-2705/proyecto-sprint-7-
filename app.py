import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header("Análisis de vehículos usados en EE. UU.")

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
if st.button("Mostrar gráfico de dispersión"):
    st.write("Gráfico de dispersión: precio vs kilometraje")

    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre kilometraje y precio"
    )

    st.plotly_chart(fig)
