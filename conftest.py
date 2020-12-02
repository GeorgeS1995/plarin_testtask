import asyncio
import json
import pytest
from main import app
from models import EmployeeModel


def get_test_data(path):
    with open(path, "r") as file:
        return json.load(file)


@pytest.fixture(scope="session")
def monkeysession(request):
    from _pytest.monkeypatch import MonkeyPatch
    mpatch = MonkeyPatch()
    yield mpatch
    mpatch.undo()


@pytest.yield_fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def prepare_test_data(monkeysession):
    monkeysession.setattr(EmployeeModel.Meta, "collection", "app_employee_test")

    with open("employees.json", "r") as file:
        employees = json.load(file)
    for e in employees[:10]:
        employee = EmployeeModel(**e)
        await employee.save()
    yield
    await app.mongodb.drop_collection("app_employee_test")
