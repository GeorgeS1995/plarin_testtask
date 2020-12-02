import json
from fastapi_contrib.db.utils import setup_mongodb
from models import EmployeeModel
from urls import router
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as err:
        return JSONResponse(content={"error": f"Internal server error: {err}"}, status_code=500)

API_V1 = "/api/v1"

app = FastAPI()
setup_mongodb(app)
app.include_router(router, prefix=API_V1)
app.middleware('http')(catch_exceptions_middleware)


async def _fill_db():
    with open("employees.json", "r") as file:
        employees = json.load(file)
    for e in employees:
        employee = EmployeeModel(**e)
        await employee.save()


@app.on_event("startup")
async def startup():
    c = await EmployeeModel.count()
    if not c:
        await _fill_db()

