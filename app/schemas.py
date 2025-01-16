# Importación de las clases necesarias de Pydantic y otros módulos
from pydantic import BaseModel  # BaseModel es la clase base de Pydantic para la validación de datos
from datetime import datetime  # Para trabajar con fechas y horas
from typing import Optional  # Para definir campos que pueden ser opcionales

# Definición de la clase base para 'Department', que es una representación de datos para la entrada de información
class DepartmentBase(BaseModel):
    name: str  # El departamento tiene un campo 'name' que es de tipo cadena

# Definición de la clase para crear un nuevo departamento (sin cambios adicionales)
class DepartmentCreate(DepartmentBase):
    pass  # Esta clase hereda de 'DepartmentBase' y no tiene campos adicionales

# Definición de la clase 'Department' que representa la entidad completa del departamento con su 'id'
class Department(DepartmentBase):
    id: int  # Agrega un campo 'id' que es un entero (esto será generado automáticamente por la base de datos)

    # Configuración para permitir que Pydantic mapee atributos directamente desde los modelos de la base de datos
    class ConfigDict:
        from_attributes = True

# Definición de la clase base para 'Job', que es una representación de datos para la entrada de información
class JobBase(BaseModel):
    title: str  # El trabajo tiene un campo 'title' que es de tipo cadena

# Definición de la clase para crear un nuevo trabajo (sin cambios adicionales)
class JobCreate(JobBase):
    pass  # Esta clase hereda de 'JobBase' y no tiene campos adicionales

# Definición de la clase 'Job' que representa la entidad completa del trabajo con su 'id'
class Job(JobBase):
    id: int  # Agrega un campo 'id' que es un entero (esto será generado automáticamente por la base de datos)

    # Configuración para permitir que Pydantic mapee atributos directamente desde los modelos de la base de datos
    class ConfigDict:
        from_attributes = True

# Definición de la clase base para 'Employee', que es una representación de datos para la entrada de información
class EmployeeBase(BaseModel):
    name: str  # El empleado tiene un campo 'name' que es de tipo cadena
    datetime: datetime  # El campo 'datetime' almacena la fecha y hora de contratación del empleado
    department_id: Optional[int] = None  # El campo 'department_id' es opcional y hace referencia a un departamento
    job_id: Optional[int] = None  # El campo 'job_id' es opcional y hace referencia a un trabajo

# Definición de la clase para crear un nuevo empleado (sin cambios adicionales)
class EmployeeCreate(EmployeeBase):
    pass  # Esta clase hereda de 'EmployeeBase' y no tiene campos adicionales

# Definición de la clase 'Employee' que representa la entidad completa del empleado con su 'id'
class Employee(EmployeeBase):
    id: int  # Agrega un campo 'id' que es un entero (esto será generado automáticamente por la base de datos)

    # Configuración para permitir que Pydantic mapee atributos directamente desde los modelos de la base de datos
    class ConfigDict:
        from_attributes = True
