from sqlalchemy.orm import Session
from app import models, schemas

def create_department(db: Session, department: schemas.Department):
    db_deparment = models.Department(
        id=department.id,
        name=department.name
    )
    db.add(db_deparment)
    db.commit()
    db.refresh(db_deparment)
    return db_deparment

def create_employee(db: Session, employee: schemas.Employee):
    db_employee = models.Employee(
        id=employee.id,
        name=employee.name,
        datetime=employee.datetime,
        department_id=employee.department_id,
        job_id=employee.job_id
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def create_job(db: Session, job: schemas.Job):
    db_job = models.Job(
        id=job.id,
        title=job.title
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_employee_by_id(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def update_employee(db: Session, employee_id: int, employee: schemas.Employee):
    db_employee = get_employee_by_id(db, employee_id)
    if db_employee:
        db_employee.name = employee.name
        db_employee.datetime = employee.datetime
        db_employee.department_id = employee.department_id
        db_employee.job_id = employee.job_id
        db.commit()
        db.refresh(db_employee)
        return db_employee
    return None
