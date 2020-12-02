import os
from starlette.testclient import TestClient
from conftest import get_test_data
from main import app
import pytest


client = TestClient(app)


class TestEmployee:
    @pytest.mark.parametrize("data", get_test_data(os.path.join(os.getcwd(), "test", "test_get_method.json")))
    def test_get_method(self, prepare_test_data, data):
        response = client.get("/api/v1/employee", params=data['input'])
        assert response.status_code == 200
        assert response.json()['result'] == data['output']
