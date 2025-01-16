# Importación de las clases necesarias para interactuar con la base de datos
from sqlalchemy.orm import Session
from app import models, schemas

# Función para crear un departamento en la base de datos
def create_department(db: Session, department: schemas.Department):
    # Crear un nuevo objeto de tipo 'Department' usando los datos del esquema proporcionado
    db_deparment = models.Department(
        id=department.id,  # Asignar el ID del departamento
        name=department.name  # Asignar el nombre del departamento
    )
    # Añadir el nuevo departamento a la sesión de la base de datos
    db.add(db_deparment)
    # Confirmar los cambios en la base de datos
    db.commit()
    # Recargar el objeto 'db_deparment' para obtener los valores actualizados (por ejemplo, el ID generado si no se proporciona)
    db.refresh(db_deparment)
    # Retornar el objeto departamento creado
    return db_deparment

# Función para crear un empleado en la base de datos
def create_employee(db: Session, employee: schemas.Employee):
    # Crear un nuevo objeto de tipo 'Employee' usando los datos del esquema proporcionado
    db_employee = models.Employee(
        id=employee.id,  # Asignar el ID del empleado
        name=employee.name,  # Asignar el nombre del empleado
        datetime=employee.datetime,  # Asignar la fecha y hora del empleado
        department_id=employee.department_id,  # Asignar el ID del departamento al que pertenece el empleado
        job_id=employee.job_id  # Asignar el ID del trabajo del empleado
    )
    # Añadir el nuevo empleado a la sesión de la base de datos
    db.add(db_employee)
    # Confirmar los cambios en la base de datos
    db.commit()
    # Recargar el objeto 'db_employee' para obtener los valores actualizados
    db.refresh(db_employee)
    # Retornar el objeto empleado creado
    return db_employee

# Función para crear un trabajo (job) en la base de datos
def create_job(db: Session, job: schemas.Job):
    # Crear un nuevo objeto de tipo 'Job' usando los datos del esquema proporcionado
    db_job = models.Job(
        id=job.id,  # Asignar el ID del trabajo
        title=job.title  # Asignar el título del trabajo
    )
    # Añadir el nuevo trabajo a la sesión de la base de datos
    db.add(db_job)
    # Confirmar los cambios en la base de datos
    db.commit()
    # Recargar el objeto 'db_job' para obtener los valores actualizados
    db.refresh(db_job)
    # Retornar el objeto trabajo creado
    return db_job

# Función para obtener un empleado por su ID desde la base de datos
def get_employee_by_id(db: Session, employee_id: int):
    # Realizar la consulta para buscar el empleado cuyo ID coincida con el proporcionado
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

# Función para actualizar la información de un empleado en la base de datos
def update_employee(db: Session, employee_id: int, employee: schemas.Employee):
    # Buscar el empleado en la base de datos utilizando la función 'get_employee_by_id'
    db_employee = get_employee_by_id(db, employee_id)
    # Si el empleado existe, actualizar sus datos
    if db_employee:
        db_employee.name = employee.name  # Actualizar el nombre del empleado
        db_employee.datetime = employee.datetime  # Actualizar la fecha y hora del empleado
        db_employee.department_id = employee.department_id  # Actualizar el ID del departamento
        db_employee.job_id = employee.job_id  # Actualizar el ID del trabajo
        # Confirmar los cambios en la base de datos
        db.commit()
        # Recargar el objeto 'db_employee' para obtener los valores actualizados
        db.refresh(db_employee)
        # Retornar el objeto empleado actualizado
        return db_employee
    # Si el empleado no existe, retornar 'None'
    return None
