from fastapi.testclient import TestClient
from api import app
from robot import Stacks
from schema import Package

client = TestClient(app)

def test_sort_package_success():
    res = client.post("/api/sort", json=Package(width_cm=10, height_cm=10, length_cm=10, mass_kg=10).model_dump())
    assert res.status_code == 200

    res_json = res.json()
    assert "stack" in res_json
    assert res_json["stack"] == Stacks.STANDARD.value

def test_sort_package_unprocessable():
    data = {"width_cm": 10}
    res = client.post("/api/sort", json=data)
    assert res.status_code == 422