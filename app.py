# app.py
import streamlit as st
from modulos.login import login
from modulos.clientes import agregar_cliente
from modulos.productos import agregar_producto
from modulos.pedidos import agregar_pedido
# Comprobamos si la sesión ya está iniciada
if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
  # Mostrar el menú lateral
  opciones = ["Ventas", "Clientes", "Productos", "Pedidos"] # Agrega más opciones si las necesitas
  seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)
  # Según la opción seleccionada, mostramos el contenido correspondiente
  if seleccion == "Ventas":
    mostrar_venta()
  elif seleccion == "Clientes":
    agregar_cliente()
  elif seleccion == "Productos":
    agregar_producto()
  elif seleccion == "Pedidos":
    agregar_pedido()
else:
# Si la sesión no está iniciada, mostrar el login
  login()
