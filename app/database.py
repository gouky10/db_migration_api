# Importación de los módulos necesarios de SQLAlchemy
from sqlalchemy import create_engine  # Para crear el motor de la base de datos
from sqlalchemy.orm import sessionmaker, declarative_base  # Para manejar sesiones y la base declarativa de modelos
import os  # Para manejar variables de entorno

# Definir la URL de la base de datos a utilizar. Se obtiene del entorno con 'os.getenv', o se usa una base de datos SQLite por defecto
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Crear el motor de la base de datos usando la URL de conexión definida
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear la clase SessionLocal que se utilizará para interactuar con la base de datos.
# 'autocommit=False' desactiva el autocompletado de transacciones y 'autoflush=False' desactiva el vaciado automático del buffer de la sesión.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la clase base de los modelos de la base de datos. Los modelos heredarán de esta clase base para definir la estructura de las tablas.
Base = declarative_base()

# Función para inicializar la base de datos, creando todas las tablas definidas en los modelos de la base de datos
def init_db():
    # Crear las tablas en la base de datos, basándose en los modelos que heredan de 'Base'
    Base.metadata.create_all(bind=engine)
