from pydantic import BaseModel
from datetime import datetime

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
    department_id: int
    job_id: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class ConfigDict:
        from_attributes = True