import pytest

def task_get_user_success(test_client):
    response = test_client.get("/api/v1/user/2")

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "support" in data
    assert isinstance(data["data"]["id"], int)

def test_get_user_not_found(test_client):
    response = test_client.get("/api/v1/user/9999") #Assuming it does not exist

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_rate_limit_exceeded(test_client):
    for _ in range(11): #limit is 10/minute
        response = test_client.get("/api/v1/user/2")

    assert response.status_code == 429
    assert response.json()["detail"] == "Rate limit exceeded"