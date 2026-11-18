from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_billboard():

    response=client.get(
        "/api/v1/billboards/granVisione"
    )

    assert response.status_code==200
    data=response.json()
    assert data["name"]=="granVisione"
