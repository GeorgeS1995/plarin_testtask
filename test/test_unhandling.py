from starlette.testclient import TestClient
from filters import EmployeeFilter
from main import app

client = TestClient(app)


def test_unhandling_error_middleware(monkeypatch):
    def get_with_error(self):
        raise Exception("Test error msg")

    monkeypatch.setattr(EmployeeFilter, "get_filter", get_with_error)
    response = client.get("/api/v1/employee")
    assert response.status_code == 500
    assert response.json() == {"error": "Internal server error: Test error msg"}
