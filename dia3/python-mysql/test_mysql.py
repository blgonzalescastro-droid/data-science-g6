import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',   # use your actual password
        database='db_g6'
    )
    print(f'Connected to database: {connection.db.decode() if hasattr(connection.db, "decode") else connection.db}')

    with connection.cursor() as cursor:
        cursor.execute("SELECT nro_documento, nombre FROM alumno")
        resultado = cursor.fetchall()
        for registro in resultado:
            print('*'*50)
            print(registro)

    connection.close()

except pymysql.MySQLError as err:
    print(f"Error: {err}")

