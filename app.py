# app.py
import streamlit as st
from modulos.login import login
from modulos.clientes import mostrar_cliente
from modulos.productos import mostrar_producto
from modulos.pedidos import mostrar_pedido
# Comprobamos si la sesión ya está iniciada
if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
  # Mostrar el menú lateral
  opciones = ["Clientes", "Productos", "Pedidos"] # Agrega más opciones si las necesitas
  seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)
  # Según la opción seleccionada, mostramos el contenido correspondiente
  if seleccion == "Clientes":
    mostrar_cliente()
  elif seleccion == "Productos":
    mostrar_producto()
  elif seleccion == "Pedidos":
    mostrar_pedido()
else:
# Si la sesión no está iniciada, mostrar el login
  login()
