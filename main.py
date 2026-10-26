
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("DATABASE_URL")

# PERSONAJES (ya insertados anteriormente)
# personajes = [
#     (1, "Luna Varela", "Alive", "Humana", "Piloto estelar", "Female",
#      "Madrid", "Nave Horizonte", None, None, None),
#     (2, "Bruno Soler", "Alive", "Humano", "Mecánico", "Male",
#      "Valencia", "Colonia Marte", None, None, None),
#     (3, "Vera Montes", "Alive", "Humana", "Exploradora", "Female",
#      "Sevilla", "Nave Horizonte", None, None, None),
#     (4, "Kiro Zenth", "Alive", "Zorblax", "Diplomático", "Male",
#      "Zorblax", "Estación Órbita", None, None, None),
#     (5, "Mira Quon", "Unknown", "Zorblax", "Cartógrafa", "Female",
#      "Zorblax", "Luna Europa", None, None, None),
#     (6, "Tarek Voss", "Dead", "Zorblax", "Guardia", "Male",
#      "Zorblax", "Ruinas de Khar", None, None, None),
#     (7, "Nébula-7", "Alive", "Androide", "Médica", "Female",
#      "Taller Central", "Nave Horizonte", None, None, None),
#     (8, "Órbita-3", "Alive", "Androide", "Analista", "Unknown",
#      "Taller Central", "Estación Órbita", None, None, None),
#     (9, "Cobalto-9", "Unknown", "Androide", "Técnico", "Male",
#      "Taller Central", "Luna Europa", None, None, None),
#     (10, "Elia Nox", "Alive", "Humana", "Científica", "Female",
#      "Bilbao", "Colonia Marte", None, None, None),
# ]

# INSERTAR PERSONAJES (comentado porque ya están insertados)
# sql = """
#     INSERT INTO characters (
#         id, name, status, species, type, gender,
#         origin_name, location_name, image, url, created
#     )
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     ON CONFLICT (id) DO NOTHING
# """

try:
    with psycopg.connect(url) as connection:
        print("Conexión establecida!")

        with connection.cursor() as cur:

            # INSERTAR (desactivado)
            # cur.executemany(sql, personajes)

            cur.execute("""
                SELECT id, name, species
                FROM characters
                ORDER BY id
                LIMIT 10
            """)

            personajes = cur.fetchall()

            print("\nPrimeros 10 personajes:")
            for personaje in personajes:
                print(personaje)

            cur.execute("SELECT COUNT(*) FROM characters")
            total = cur.fetchone()[0]

            print(f"\nTotal de personajes guardados: {total}")

except Exception as e:
    print("Error:", e)
    raise