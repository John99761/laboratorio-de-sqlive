import sqlite3 as dbJohn


conexion = dbJohn.connect("Dealer.db")
cursor = conexion.cursor()


cursor.execute("DROP TABLE IF EXISTS Cliente")
cursor.execute("DROP TABLE IF EXISTS Vehículo")


cursor.execute("""CREATE TABLE IF NOT EXISTS Cliente (
               id_cliente INTEGER PRIMARY KEY,
               nombre TEXT,
               apellido TEXT,
               direccion TEXT,
               telefono TEXT,
               email TEXT
               )""")


cursor.execute('''CREATE TABLE IF NOT EXISTS Vehículo (
    id_vehiculo INTEGER PRIMARY KEY,
    marca TEXT,
    modelo TEXT,
    año INTEGER,
    matricula TEXT,
    id_cliente INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
)
''')


clientes = [
   (1, "Carlos", "Gomez", "Santo Domingo", "8295551234", "carlos.gomez@example.com"),
   (2, "Ana", "Lopez", "Santiago", "8295555678", "ana.lopez@example.com"),
   (3, "Luis", "Martinez", "La Vega", "8295558765", "luis.martinez@example.com"),
   (4, "Marta", "Perez", "Bávaro", "8295554321", "marta.perez@example.com"),
   (5, "Juan", "Hernandez", "Punta Cana", "8295556789", "juan.hernandez@example.com"),
   (6, "Sofia", "Sanchez", "Puerto Plata", "8295553456", "sofia.sanchez@example.com"),
   (7, "Miguel", "Torres", "Samana", "8295557890", "miguel.torres@example.com"),
   (8, "Lucia", "Ramirez", "Jarabacoa", "8295550987", "lucia.ramirez@example.com"),
   (9, "Diego", "Vasquez", "Higuey", "8295556543", "diego.vasquez@example.com"),
   (10, "Elena", "Fernandez", "Constanza", "8295553210", "elena.fernandez@example.com")
]


cursor.executemany("INSERT OR REPLACE INTO Cliente(id_cliente, nombre, apellido, direccion, telefono, email) VALUES (?, ?, ?, ?, ?, ?)", clientes)


vehiculos = [
    (1, "Toyota", "Corolla", 2018, "ABC123", 1),
    (2, "Honda", "Civic", 2019, "DEF456", 2),
    (3, "Ford", "Focus", 2020, "GHI789", 3),
    (4, "Chevrolet", "Malibu", 2021, "JKL012", 4),
    (5, "Nissan", "Sentra", 2017, "MNO345", 5),
    (6, "Hyundai", "Elantra", 2016, "PQR678", 6),
    (7, "Kia", "Optima", 2015, "STU901", 7),
    (8, "Volkswagen", "Jetta", 2014, "VWX234", 8),
    (9, "BMW", "3 Series", 2013, "YZA567", 9),
    (10, "Mercedes", "C Class", 2012, "BCD890", 10)
]


cursor.executemany("INSERT OR REPLACE INTO Vehículo(id_vehiculo, marca, modelo, año, matricula, id_cliente) VALUES (?, ?, ?, ?, ?, ?)", vehiculos)
cursor.execute("UPDATE Vehículo SET año = 2020 WHERE id_vehiculo = 3")

cursor.execute("""
    UPDATE Cliente
    SET nombre = 'Marcos', apellido ='Martinez' ,direccion = 'Santo Domingo oeste'
    WHERE id_cliente = 1
""")


cursor.execute("""
    UPDATE Cliente
    SET telefono = '8295554321'
    WHERE id_cliente = 2
""")

cursor.execute("""
    UPDATE Vehículo
    SET marca = 'Mercedes', modelo = 'AMG', año = 2020
    WHERE id_cliente = 1
""")

cursor.execute("""
    UPDATE Vehículo
    SET matricula = 'AF254656'
    WHERE id_cliente = 1
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cliente_temp (
        id_cliente INTEGER PRIMARY KEY,
        nombre TEXT,
        apellido TEXT,
        telefono TEXT,
        email TEXT
    )
""")

cursor.execute("""
    INSERT INTO Cliente_temp (id_cliente, nombre, apellido, telefono, email)
    SELECT id_cliente, nombre, apellido, telefono, email
    FROM Cliente
""")

# 3. Eliminar la tabla original
cursor.execute("DROP TABLE Cliente")

# 4. Renombrar la nueva tabla para que tenga el nombre de la tabla original
cursor.execute("ALTER TABLE Cliente_temp RENAME TO Cliente")

conexion.commit()
conexion.close()
