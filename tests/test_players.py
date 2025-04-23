from fastapi.testclient import TestClient

def test_create_player(client: TestClient):
    response = client.post(
        "/api/players",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "age": 25,
            "nationality": "English",
            "position": "Forward"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "John"
    assert data["last_name"] == "Doe"
    assert data["age"] == 25
    assert data["nationality"] == "English"
    assert data["position"] == "Forward"
    assert "id" in data

def test_create_player_duplicate(client: TestClient):
    # Create first player
    r1 = client.post(
        "/api/players",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "age": 25,
            "nationality": "English",
            "position": "Forward"
        }
    )
    print("fist player response:", r1.status_code)
    # Try to create duplicate
    response = client.post(
        "/api/players",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "age": 25,
            "nationality": "English",
            "position": "Forward"
        }
    )
    print("second player response:", response.status_code)
    assert response.status_code == 400
    assert response.json()["detail"] == "Player already exists"

def test_get_players(client: TestClient):
    # Create a player first
    client.post(
        "/api/players",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "age": 25,
            "nationality": "English",
            "position": "Forward"
        }
    )
    
    response = client.get("/api/players")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["first_name"] == "John"
    assert data[0]["last_name"] == "Doe"

def test_get_player(client: TestClient):
    # Create a player first
    create_response = client.post(
        "/api/players",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "age": 25,
            "nationality": "English",
            "position": "Forward"
        }
    )
    player_id = create_response.json()["id"]
    
    response = client.get(f"/api/players/{player_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == player_id
    assert data["first_name"] == "John"
    assert data["last_name"] == "Doe"

def test_get_player_not_found(client: TestClient):
    response = client.get("/api/players/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Player not found"

def test_update_player(client: TestClient):
    # Create a player first
    create_response = client.post(
        "/api/players",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "age": 25,
            "nationality": "English",
            "position": "Forward"
        }
    )
    player_id = create_response.json()["id"]
    
    # Update the player
    response = client.put(
        f"/api/players/{player_id}",
        json={
            "first_name": "Jane",
            "age": 26
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == player_id
    assert data["first_name"] == "Jane"
    assert data["age"] == 26
    assert data["last_name"] == "Doe"  # Should remain unchanged

def test_update_player_not_found(client: TestClient):
    response = client.put(
        "/api/players/999",
        json={
            "first_name": "Jane"
        }
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Player not found"

def test_delete_player(client: TestClient):
    # Create a player first
    create_response = client.post(
        "/api/players",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "age": 25,
            "nationality": "English",
            "position": "Forward"
        }
    )
    player_id = create_response.json()["id"]
    
    # Delete the player
    response = client.delete(f"/api/players/{player_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Player deleted successfully"
    
    # Verify player is deleted
    get_response = client.get(f"/api/players/{player_id}")
    assert get_response.status_code == 404

def test_delete_player_not_found(client: TestClient):
    response = client.delete("/api/players/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Player not found" 