import streamlit as st
from modulos.config.conexion import obtener_conexion
def mostrar_cliente():
    st.header("👤 Registrar cliente")
    try:
        con = obtener_conexion()
        cursor = con.cursor()
        # Formulario para registrar el cliente
        with st.form("form_cliente"):
            nombre = st.text_input("Nombre")
            telefono = st.text_input("Teléfono")
            correo = st.text_input("Correo")
            enviar = st.form_submit_button("✅ Guardar cliente")
            if enviar:
                if nombre.strip() == "":
                    st.warning("⚠️ Debes ingresar el nombre del cliente.")
                else:
                    try:
                        cursor.execute(
                            "INSERT INTO Clientes (nombre, telefono, correo) VALUES (%s, %s, %s)",
                            (nombre, telefono, correo)
                        )
                        con.commit()
                        st.success(f"✅ Cliente registrado correctamente: {nombre}")
                        st.rerun()
                    except Exception as e:
                        con.rollback()
                        st.error(f"❌ Error al registrar el cliente: {e}")
        # Mostrar los registros existentes
        st.subheader("📋 Clientes registrados")
        cursor.execute("SELECT id_cliente, nombre, telefono, correo FROM Clientes")
        registros = cursor.fetchall()
        st.dataframe(registros)
    except Exception as e:
        st.error(f"❌ Error general: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()
