# Importación de los módulos necesarios de SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime  # Para definir tipos de columnas y claves foráneas
from sqlalchemy.orm import relationship  # Para establecer relaciones entre tablas
from app.database import Base  # Importación de la clase Base para que los modelos hereden de ella

# Definición de la clase 'Department', que representa la tabla 'departments' en la base de datos
class Department(Base):
    __tablename__ = 'departments'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True, index=True)  # Columna 'id' que es la clave primaria y tiene un índice
    name = Column(String, index=True)  # Columna 'name' que tiene un índice para optimizar las consultas

# Definición de la clase 'Job', que representa la tabla 'jobs' en la base de datos
class Job(Base):
    __tablename__ = 'jobs'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True, index=True)  # Columna 'id' que es la clave primaria y tiene un índice
    title = Column(String, index=True)  # Columna 'title' que tiene un índice para optimizar las consultas

# Definición de la clase 'Employee', que representa la tabla 'employees' en la base de datos
class Employee(Base):
    __tablename__ = 'employees'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True, index=True)  # Columna 'id' que es la clave primaria y tiene un índice
    name = Column(String, index=True)  # Columna 'name' que tiene un índice para optimizar las consultas
    datetime = Column(DateTime)  # Columna 'datetime' para almacenar fechas y horas
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=True)  # Columna 'department_id' que es una clave foránea que hace referencia a la tabla 'departments'
    job_id = Column(Integer, ForeignKey('jobs.id'), nullable=True)  # Columna 'job_id' que es una clave foránea que hace referencia a la tabla 'jobs'

    # Establecimiento de relaciones entre la tabla 'employees' y las tablas 'departments' y 'jobs'
    department = relationship('Department')  # Relación con la tabla 'Department'
    job = relationship('Job')  # Relación con la tabla 'Job'
