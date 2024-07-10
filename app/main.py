from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
import app.crud as crud, app.models as models, app.schemas as schemas
from app.database import SessionLocal, engine, init_db
from typing import List, Dict
from pydantic import ValidationError
import pandas as pd
import os

app = FastAPI()

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload_departments/")
async def upload_departments(file: UploadFile = File(...), db: Session = Depends(get_db)):
    directory_path='/migration/tmp/'
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    file_location = f"{directory_path}{file.filename}"
    with open(file_location, "wb") as file_object:
        content = await file.read()
        file_object.write(content)

    column_names = ["id", "name"]
    df = pd.read_csv(file_location, header=None, names=column_names)

    for index, row in df.iterrows():
        department = schemas.Department(
            id=row['id'],
            name=row['name']
        )
        crud.create_department(db=db, department=department)
    return {"message": "File uploaded successfully"}

@app.post("/upload_jobs/")
async def upload_jobs(file: UploadFile = File(...), db: Session = Depends(get_db)):
    directory_path='/migration/tmp/'
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    file_location = f"{directory_path}{file.filename}"
    with open(file_location, "wb") as file_object:
        content = await file.read()
        file_object.write(content)

    column_names = ["id", "title"]
    df = pd.read_csv(file_location, header=None, names=column_names)

    for index, row in df.iterrows():
        job = schemas.Job(
            id=row['id'],
            title=row['title']
        )
        crud.create_job(db=db, job=job)
    return {"message": "File uploaded successfully"}

@app.post("/upload_employees/")
async def upload_employees(file: UploadFile = File(...), db: Session = Depends(get_db)):
    directory_path='/migration/tmp/'
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    file_location = f"{directory_path}{file.filename}"
    with open(file_location, "wb") as file_object:
        content = await file.read()
        file_object.write(content)

    column_names = ["id", "name", "datetime", "department_id", "job_id"]
    df = pd.read_csv(file_location, header=None, names=column_names)
    
    errors: List[Dict] = []

    for index, row in df.iterrows():
        try:
            employee = schemas.Employee(
                id=row['id'],
                name=row['name'] if pd.notna(row['name']) else None,
                datetime=row['datetime'] if pd.notna(row['datetime']) else None,
                department_id=row['department_id'] if pd.notna(row['department_id']) else None,
                job_id=row['job_id'] if pd.notna(row['job_id']) else None
            )
            existing_employee = crud.get_employee_by_id(db=db, employee_id=employee.id)
            if existing_employee:
                crud.update_employee(db=db, employee_id=employee.id, employee=employee)
            else:
                crud.create_employee(db=db, employee=employee)
        except ValidationError as e:
            errors.append({
                "row": index + 1,
                "errors": e.errors()
            })
    
    if errors:
        return {"message": "File uploaded with some errors", "errors": errors}
    return {"message": "File uploaded successfully"}


'''@app.post("/departments/", response_model=schemas.Department)
def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db=db, department=department)

@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)'''

from fastapi import Query
from sqlalchemy import func, case

@app.get("/metrics/hires_per_quarter/")
def hires_per_quarter(year: int, db: Session = Depends(get_db)):
    result = db.query(
        models.Department.name.label('department'),
        models.Job.title.label('job'),
        func.sum(case((func.extract('quarter', models.Employee.datetime) == 1, 1), else_=0)).label('Q1'),
        func.sum(case((func.extract('quarter', models.Employee.datetime) == 2, 1), else_=0)).label('Q2'),
        func.sum(case((func.extract('quarter', models.Employee.datetime) == 3, 1), else_=0)).label('Q3'),
        func.sum(case((func.extract('quarter', models.Employee.datetime) == 4, 1), else_=0)).label('Q4')
    ).join(models.Employee.department).join(models.Employee.job).filter(
        func.extract('year', models.Employee.datetime) == year
    ).group_by(models.Department.name, models.Job.title).order_by(models.Department.name, models.Job.title).all()
    
    response = []
    for row in result:
        response.append({
            "department": row.department,
            "job": row.job,
            "Q1": row.Q1,
            "Q2": row.Q2,
            "Q3": row.Q3,
            "Q4": row.Q4
        })
    
    return response

@app.get("/metrics/departments_above_mean/")
def departments_above_mean(year: int, db: Session = Depends(get_db)):
    subquery = db.query(
        models.Department.id,
        models.Department.name.label('department'),
        func.count(models.Employee.id).label('hired')
    ).join(models.Employee.department).filter(
        func.extract('year', models.Employee.datetime) == year
    ).group_by(models.Department.id, models.Department.name).subquery()

    mean_hires = db.query(func.avg(subquery.c.hired)).scalar()

    result = db.query(
        subquery.c.id,
        subquery.c.department,
        subquery.c.hired
    ).filter(subquery.c.hired > mean_hires).order_by(subquery.c.hired.desc()).all()

    response = []
    for row in result:
        response.append({
            "id": row.id,
            "department": row.department,
            "hired": row.hired
        })

    return response
