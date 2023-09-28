import psycopg2

conn = psycopg2.connect(
    user="postgres", password="Franmillan", port="5432", host="localhost", database="curso"
)

cursor = conn.cursor()

# Create table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS clientes (id SERIAL PRIMARY KEY, name VARCHAR(255), age INTEGER, email VARCHAR(255))"
)

cursor.execute(
    "CREATE TABLE IF NOT EXISTS proveedores (id SERIAL PRIMARY KEY, name VARCHAR(255), age INTEGER, email VARCHAR(255))"
)


# Save data
conn.commit()


# Insert data

for i in range (10):
    contador = 0
    cursor.execute(
            "INSERT INTO clientes (name, age, email) VALUES (%s, %s, %s)",
            ("Juan", contador, "juan"+"@mail.com"),
    )
    contador += 1

for i in range (10):
    contador = 0
    cursor.execute(
            "INSERT INTO proveedores (name, age, email) VALUES (%s, %s, %s)",
            ("Juan", contador, "juan"+"@mail.com"),
    )
    contador += 1



# fetch and print data
cursor.execute("SELECT * FROM clientes")
print(cursor.fetchall())
#
# # fetch one
cursor.execute("SELECT * FROM clientes wHERE name=%s", ("Juan",))
print(cursor.fetchone())


# Update

cursor.execute(
    "UPDATE clientes SET name = 'Fran' WHERE name='Juan'"
)

cursor.execute("SELECT * FROM clientes wHERE name=%s", ("Fran",))
print(cursor.fetchone())