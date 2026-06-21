import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='bba9yarouk7qhymw9e8t-mysql.services.clever-cloud.com',
            user='u9db98cr4atsdd8o',
            password='0Femfy3VC9YVOj3dzeaH',
            database='bba9yarouk7qhymw9e8t',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None
