import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

hist_button = st.button('Construir histograma') # crear un botón
disper_button = st.button('Construir grafico de dispersion') # crear un botón

st.header('Gráficos para el análisis de los vehículos')

if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
# crear un histograma
    fig = px.histogram(car_data, x="odometer")

 # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disper_button: # al hacer clic en el botón
    st.write('Creación de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')
            
# crear un histograma
    fig = px.scatter(car_data, x="odometer", y='price')

 # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)