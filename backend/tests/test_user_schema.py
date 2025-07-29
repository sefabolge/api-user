# Ensure returned user schema matches your Pydantic model

def test_user_response_contract(test_client):
    response = test_client.get("/api/v1/user/4")
    data = response.json()

    assert isinstance(data["data"]["id"], int)
    assert isinstance(data["data"]["first_name"], str)
    assert isinstance(data["support"]["url"], str)
