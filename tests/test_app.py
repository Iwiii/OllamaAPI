import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_hello_world(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, World!"}

    def test_create_user(self):
        response = self.client.post("/users", json={"name": "John Doe", "email": "john.doe@example.com"})
        assert response.status_code == 201
        assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

    def test_get_user(self):
        response = self.client.get("/users/1")
        assert response.status_code == 200
        assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

    def test_update_user(self):
        response = self.client.put("/users/1", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
        assert response.status_code == 200
        assert response.json() == {"id": 1, "name": "Jane Doe", "email": "jane.doe@example.com"}

    def test_delete_user(self):
        response = self.client.delete("/users/1")
        assert response.status_code == 204

if __name__ == "__main__":
    unittest.main()