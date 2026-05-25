"""Script para crear la base de datos de Cine Multiplex con datos iniciales."""

import sqlite3
from pathlib import Path

# Eliminar la base de datos si ya existe (para recrearla limpia)
ruta_bd = Path("cine.db")
if ruta_bd.exists():
    ruta_bd.unlink()

conn = sqlite3.connect("cine.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# Crear tablas (en el orden correcto: sin dependencias primero, luego con dependencias)
cursor.executescript("""
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS peliculas (
    titulo TEXT PRIMARY KEY,
    duracion_minutos INTEGER NOT NULL,
    clasificacion TEXT NOT NULL,
    genero TEXT NOT NULL,
    esta_en_cartelera INTEGER NOT NULL DEFAULT 1,
    tipo_pelicula TEXT NOT NULL,
    distribuidora TEXT,
    edad_minima INTEGER,
    anio_lanzamiento INTEGER
);

CREATE TABLE IF NOT EXISTS salas (
    numero INTEGER PRIMARY KEY,
    capacidad_maxima INTEGER NOT NULL,
    tecnologia_pantalla TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sesiones (
    id_sesion TEXT PRIMARY KEY,
    pelicula_titulo TEXT NOT NULL,
    sala_numero INTEGER NOT NULL,
    fecha_hora TEXT NOT NULL,
    numero_asientos_ocupados INTEGER NOT NULL DEFAULT 0,
    estado_sesion TEXT NOT NULL DEFAULT 'programada',
    FOREIGN KEY (pelicula_titulo) REFERENCES peliculas(titulo),
    FOREIGN KEY (sala_numero) REFERENCES salas(numero)
);

CREATE TABLE IF NOT EXISTS entradas (
    id_entrada TEXT PRIMARY KEY,
    sesion_id TEXT NOT NULL,
    precio_euros REAL NOT NULL,
    categoria_tarifa TEXT NOT NULL,
    fecha_venta TEXT NOT NULL,
    FOREIGN KEY (sesion_id) REFERENCES sesiones(id_sesion)
);
""")

# Insertar datos iniciales

# 1. Crear películas (una de cada subtipo, igual que en datos_iniciales.py)
cursor.execute("""
    INSERT INTO peliculas
    (titulo, duracion_minutos, clasificacion, genero, esta_en_cartelera,
     tipo_pelicula, distribuidora, edad_minima, anio_lanzamiento)
    VALUES ('Dune: Parte Dos', 166, 'PG-13', 'Ciencia Ficción', 1,
            'COMERCIAL', 'Warner Bros', NULL, NULL)
""")

cursor.execute("""
    INSERT INTO peliculas
    (titulo, duracion_minutos, clasificacion, genero, esta_en_cartelera,
     tipo_pelicula, distribuidora, edad_minima, anio_lanzamiento)
    VALUES ('Kung Fu Panda 4', 94, 'PG', 'Animación', 1,
            'INFANTIL', NULL, 5, NULL)
""")

cursor.execute("""
    INSERT INTO peliculas
    (titulo, duracion_minutos, clasificacion, genero, esta_en_cartelera,
     tipo_pelicula, distribuidora, edad_minima, anio_lanzamiento)
    VALUES ('El Padrino', 175, 'R', 'Crimen', 1,
            'CLASICA', NULL, NULL, 1972)
""")

# 2. Crear salas
cursor.execute("INSERT INTO salas (numero, capacidad_maxima, tecnologia_pantalla) VALUES (1, 100, '2D')")
cursor.execute("INSERT INTO salas (numero, capacidad_maxima, tecnologia_pantalla) VALUES (2, 50, '3D')")
cursor.execute("INSERT INTO salas (numero, capacidad_maxima, tecnologia_pantalla) VALUES (3, 30, 'IMAX')")

# 3. Crear una sesión de ejemplo
cursor.execute("""
    INSERT INTO sesiones (id_sesion, pelicula_titulo, sala_numero, fecha_hora,
                          numero_asientos_ocupados, estado_sesion)
    VALUES ('S001', 'Dune: Parte Dos', 1, '2026-04-20 18:00', 0, 'programada')
""")

conn.commit()
conn.close()

print("Base de datos creada en: cine.db")
