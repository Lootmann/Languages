from fastapi import status
from fastapi.testclient import TestClient
from main import app


class TestHoge:
    def test_create_hero(self, client: TestClient):
        resp = client.post("/heroes", json={"name": "hoge", "secret_name": "hogege"})
        app.dependency_overrides.clear()
        data = resp.json()

        assert resp.status_code == status.HTTP_200_OK
        assert data["name"] == "hoge"
        assert data["secret_name"] == "hogege"
        assert data["id"] is not None
