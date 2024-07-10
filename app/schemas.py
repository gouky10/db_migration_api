from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int

    class ConfigDict:
        from_attributes = True

class JobBase(BaseModel):
    title: str

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int

    class ConfigDict:
        from_attributes = True

class EmployeeBase(BaseModel):
    name: str
    datetime: datetime
    department_id: Optional[int] = None 
    job_id: Optional[int] = None 

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class ConfigDict:
        from_attributes = True