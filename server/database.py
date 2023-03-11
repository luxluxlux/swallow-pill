import psycopg2

def connect_to_database(configuration):
    conn = psycopg2.connect(**configuration)
    cursor = conn.cursor()

    # TODO Clear, test connection
    cursor.execute('SELECT * FROM users')
    print(cursor.fetchall())

    cursor.close()
    conn.close()
