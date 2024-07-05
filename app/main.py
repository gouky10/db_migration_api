from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import app.crud as crud, app.models as models, app.schemas as schemas
from app.database import SessionLocal, engine, init_db
import pandas as pd

app = FastAPI()

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

@app.post("/upload/")
def upload_csv(file_path: str, db: Session = Depends(get_db)):
    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        employee = schemas.EmployeeCreate(
            name=row['name'],
            datetime=row['datetime'],
            department_id=row['department_id'],
            job_id=row['job_id']
        )
        crud.create_employee(db=db, employee=employee)
    return {"message": "File uploaded successfully"}