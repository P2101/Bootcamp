# pip install PyMySQL
import pymysql

def get_name(name):
    host = 'localhost'
    port = 3306
    user = 'root'
    password = 'root' 

    connection = pymysql.connect(host=host,
                                port=port,
                                user=user,
                                password=password)

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS historial")

    cursor.execute("USE historial")

    table_query = """
    CREATE TABLE IF NOT EXISTS data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        winner VARCHAR(100) NOT NULL,
        loser VARCHAR(100) NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """

    cursor.execute(table_query)
    print("El ganador es:", name[0])
    cursor = connection.cursor()

    insert_query = "INSERT INTO data (winner, loser) VALUES (%s, %s)"
    cursor.execute(insert_query, (name[0], name[1]))

    connection.commit()
    cursor.close()
    connection.close()
