import psycopg2

def create_db():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clients (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(50),
        phone_numbers VARCHAR(255)[]
        )
    """)
    conn.commit()

def add_client(first_name, last_name, email, phone_numbers=[]):
    cur.execute("""
        INSERT INTO clients (first_name, last_name, email, phone_numbers)
        VALUES (%s, %s, %s, %s) RETURNING id
    """, (first_name, last_name, email, phone_numbers))
    client_id = cur.fetchone()[0]
    conn.commit()
    return client_id

def add_phone(client_id, phone_number):
    cur.execute("""
        UPDATE clients SET phone_numbers = array_append(phone_numbers, %s) WHERE id = %s

    """, (phone_number, client_id))
    conn.commit()

def change_client(client_id, first_name=None, last_name=None, email=None):
    updates = []
    if first_name:
        updates.append("first_name = %s")
    if last_name:
        updates.append("last_name = %s")
    if email:
        updates.append("email = %s")
    if not updates:
        pass
    query = """
    UPDATE clients set {}
    WHERE id = %s
    """.format(", ".join(updates))
    cur.execute(query, tuple(filter(None, [first_name, last_name, email, client_id])))
    conn.commit()

def delete_phone(client_id, phone_number):
    cur.execute("""
        UPDATE clients SET phone_numbers = array_remove(phone_numbers, %s) WHERE id = %s
    """, (phone_number, client_id))
    conn.commit()

def delete_client(client_id):
    cur.execute("""
        DELETE FROM clients WHERE id = %s
    """, (client_id))
    conn.commit()

def find_client(query):
    cur.execute("""
        SELECT * FROM clients
        WHERE first_name ILIKE %s OR last_name ILIKE %s OR email ILIKE %s OR phone_numbers @> ARRAY[%s]::VARCHAR[]
    """, (f"%{query}%", f"%{query}%", f"%{query}%", query))
    print(cur.fetchall())

conn = psycopg2.connect(database="netology", user="postgres", password="Qwerty")
cur = conn.cursor()
create_db()
add_client("Сергей", "Сергеев", "sergeev@mail.ru", ["11111111", "22222223"])
add_client("Иван", "Иванв", "ivanv@mail.ru", ["33333333", "44444444"])
add_client("Степан", "Степанов", "stepanov@mail.ru", ["55555555", "66666666"])
add_client("Андрей", "Андреев", "andreev@mail.ru", ["77777777", "88888888"])
add_phone("1", "22222222")
change_client("2", "Иван", "Иванов", "ivanov@mail.ru")
delete_phone("1", "22222223")
delete_client("3")
find_client("Иванов")
conn.close()