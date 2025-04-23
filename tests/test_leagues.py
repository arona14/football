from fastapi.testclient import TestClient

def test_create_league(client: TestClient):
    response = client.post(
        "/api/leagues",
        json={
            "name": "Premier League",
            "country_name": "England",
            "level": 1,
            "country_code": "GB",
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Premier League"
    assert data["country_name"] == "England"
    assert data["level"] == 1
    assert "id" in data

def test_create_league_duplicate(client: TestClient):
    # Create first league
    client.post(
        "/api/leagues",
        json={
            "name": "Premier League",
            "country_name": "England",
            "level": 1,
            "country_code": "GB",
        }
    )
    
    # Try to create duplicate
    response = client.post(
        "/api/leagues",
        json={
            "name": "Premier League",
            "country_name": "England",
            "level": 1,
            "country_code": "GB",
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "League already exists"

def test_get_leagues(client: TestClient):
    # Create a league first
    client.post(
        "/api/leagues",
        json={
            "name": "Premier League",
            "country_name": "England",
            "level": 1,
            "country_code": "GB",
        }
    )
    
    response = client.get("/api/leagues")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["name"] == "Premier League"
    assert data[0]["country_name"] == "England"

def test_get_league(client: TestClient):
    # Create a league first
    create_response = client.post(
        "/api/leagues",
        json={
            "name": "Premier League",
            "country_name": "England",
            "level": 1,
            "country_code": "GB",
        }
    )
    league_id = create_response.json()["id"]
    
    response = client.get(f"/api/leagues/{league_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == league_id
    assert data["name"] == "Premier League"
    assert data["country_name"] == "England"

def test_get_league_not_found(client: TestClient):
    response = client.get("/api/leagues/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "League not found"

def test_update_league(client: TestClient):
    # Create a league first
    create_response = client.post(
        "/api/leagues",
        json={
            "name": "Premier League",
            "country_name": "England",
            "level": 1,
            "country_code": "GB",
        }
    )
    league_id = create_response.json()["id"]
    
    # Update the league
    response = client.put(
        f"/api/leagues/{league_id}",
        json={
            "name": "English Premier League",
            "country_code": "UK",
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == league_id
    assert data["name"] == "English Premier League"
    assert data["country_code"] == "UK"

def test_update_league_not_found(client: TestClient):
    response = client.put(
        "/api/leagues/999",
        json={
            "name": "English Premier League"
        }
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "League not found"

def test_delete_league(client: TestClient):
    # Create a league first
    create_response = client.post(
        "/api/leagues",
        json={
            "name": "Premier League",
            "country_name": "England",
            "level": 1,
            "country_code": "GB",
        }
    )
    league_id = create_response.json()["id"]
    
    # Delete the league
    response = client.delete(f"/api/leagues/{league_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "League deleted"
    
    # Verify league is deleted
    get_response = client.get(f"/api/leagues/{league_id}")
    assert get_response.status_code == 404

def test_delete_league_not_found(client: TestClient):
    response = client.delete("/api/leagues/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "League not found" 