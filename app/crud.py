from sqlalchemy.orm import Session
from app import models, schemas

def create_department(db: Session, department: schemas.DepartmentCreate):
    db_deparment = models.Department(name=department.name)
    db.add(db_deparment)
    db.commit()
    db.refresh(db_deparment)
    return db_deparment

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        name=employee.name,
        datetime=employee.datetime,
        department_id=employee.department_id,
        job_id=employee.job_id
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(title=job.title)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job