import streamlit as st
import pandas as pd
from modulos.config.conexion import obtener_conexion
def mostrar_pedido():
    st.header("🧾 Registrar pedido")
    try:
        con = obtener_conexion()
        cursor = con.cursor()
        # Formulario para registrar el pedido
        with st.form("form_pedido"):
            id_cliente = st.number_input("ID Cliente", min_value=1, step=1)
            id_producto = st.number_input("ID Producto", min_value=1, step=1)
            cantidad = st.number_input("Cantidad", min_value=1, step=1)
            fecha = st.date_input("Fecha")
            enviar = st.form_submit_button("✅ Guardar pedido")
            if enviar:
                try:
                    cursor.execute(
                        "INSERT INTO Pedidos (id_cliente, id_producto, cantidad, fecha) VALUES (%s, %s, %s, %s)",
                        (id_cliente, id_producto, cantidad, fecha)
                    )
                    con.commit()
                    st.success("✅ Pedido registrado correctamente")
                    st.rerun()
                except Exception as e:
                    con.rollback()
                    st.error(f"❌ Error al registrar el pedido: {e}")
        # Mostrar los registros existentes
        st.subheader("📋 Pedidos registrados")
        cursor.execute("SELECT id_pedido, id_cliente, id_producto, cantidad, fecha FROM Pedidos")
        registros = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(registros, columns=columnas)
        st.dataframe(df)
    except Exception as e:
        st.error(f"❌ Error general: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()
