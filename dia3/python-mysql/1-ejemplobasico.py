import pymysql

# --- Create connection to the database ---
try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root2025',   # use your actual password
        database='db_g6'
    )

    print(f'Estás conectado a la base de datos {connection.db.decode() if hasattr(connection.db, "decode") else connection.db}')

    # --- Insert data (uncomment if you want to insert) ---
    # with connection.cursor() as alumno_cursor:
    #     alumno_cursor.execute("INSERT INTO alumno(nro_documento, nombre) VALUES ('1002', 'Jesus Lopez')")
    #     connection.commit()
    #     print("Alumno insertado")

    # --- Select and display data ---
    with connection.cursor() as alumno_cursor_select:
        alumno_cursor_select.execute("SELECT nro_documento, nombre FROM alumno")
        resultado = alumno_cursor_select.fetchall()
        for registro in resultado:
            print('*'*50)
            print(f'DNI    : {registro[0]}')
            print(f'NOMBRE : {registro[1]}')

finally:
    # --- Close connection ---
    connection.close()
