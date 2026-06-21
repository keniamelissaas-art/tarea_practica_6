import streamlit as st
from modulos.config.conexion import obtener_conexion
def mostrar_producto():
    st.header("📦 Registrar producto")
    try:
        con = obtener_conexion()
        cursor = con.cursor()
        # Formulario para registrar el producto
        with st.form("form_producto"):
            nombre = st.text_input("Nombre del producto")
            precio = st.number_input("Precio", min_value=0.0, step=0.01)
            stock = st.number_input("Stock", min_value=0, step=1)
            enviar = st.form_submit_button("✅ Guardar producto")
            if enviar:
                if nombre.strip() == "":
                    st.warning("⚠️ Debes ingresar el nombre del producto.")
                else:
                    try:
                        cursor.execute(
                            "INSERT INTO Productos (nombre, precio, stock) VALUES (%s, %s, %s)",
                            (nombre, precio, stock)
                        )
                        con.commit()
                        st.success(f"✅ Producto registrado correctamente: {nombre}")
                        st.rerun()
                    except Exception as e:
                        con.rollback()
                        st.error(f"❌ Error al registrar el producto: {e}")
        # Mostrar los registros existentes
        st.subheader("📋 Productos registrados")
        cursor.execute("SELECT id_producto, nombre, precio, stock FROM Productos")
        registros = cursor.fetchall()
        st.dataframe(registros)
    except Exception as e:
        st.error(f"❌ Error general: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()
