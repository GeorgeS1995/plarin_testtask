from datetime import datetime
from fastapi_contrib.db.models import MongoDBModel


class EmployeeModel(MongoDBModel):
    name: str = None
    email: str = None
    age: int = None
    company: str = None
    join_date: datetime = None
    job_title: str = None
    gender: str = None
    salary: int = None

    class Meta:
        collection = "app_employee"
