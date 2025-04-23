from fastapi.testclient import TestClient

def test_create_team(client: TestClient):
    response = client.post(
        "/api/teams",
        json={
            "name": "Manchester United",
            "city": "Manchester",
            "country": "England",
            "founded_year": "1878"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Manchester United"
    assert data["city"] == "Manchester"
    assert data["country"] == "England"
    assert data["founded_year"] == "1878"
    assert "id" in data

def test_create_team_duplicate(client: TestClient):
    # Create first team
    client.post(
        "/api/teams",
        json={
            "name": "Manchester United",
            "city": "Manchester",
            "country": "England",
            "founded_year": "1878"
        }
    )
    
    # Try to create duplicate
    response = client.post(
        "/api/teams",
        json={
            "name": "Manchester United",
            "city": "Manchester",
            "country": "England",
            "founded_year": "1878"
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Team already exists"

def test_get_teams(client: TestClient):
    # Create a team first
    client.post(
        "/api/teams",
        json={
            "name": "Manchester United",
            "city": "Manchester",
            "country": "England",
            "founded_year": "1878"
        }
    )
    
    response = client.get("/api/teams")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["name"] == "Manchester United"
    assert data[0]["city"] == "Manchester"

def test_get_team(client: TestClient):
    # Create a team first
    create_response = client.post(
        "/api/teams",
        json={
            "name": "Manchester United",
            "city": "Manchester",
            "country": "England",
            "founded_year": "1878"
        }
    )
    team_id = create_response.json()["id"]
    
    response = client.get(f"/api/teams/{team_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == team_id
    assert data["name"] == "Manchester United"
    assert data["city"] == "Manchester"

def test_get_team_not_found(client: TestClient):
    response = client.get("/api/teams/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Team not found"

def test_update_team(client: TestClient):
    # Create a team first
    create_response = client.post(
        "/api/teams",
        json={
            "name": "Manchester United",
            "city": "Manchester",
            "country": "England",
            "founded_year": "1878"
        }
    )
    team_id = create_response.json()["id"]
    
    # Update the team
    response = client.put(
        f"/api/teams/{team_id}",
        json={
            "name": "Man United",
            "founded_year": "1880"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == team_id
    assert data["name"] == "Man United"
    assert data["founded_year"] == "1880"
    assert data["city"] == "Manchester"  # Should remain unchanged

def test_update_team_not_found(client: TestClient):
    response = client.put(
        "/api/teams/999",
        json={
            "name": "Man United"
        }
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Team not found"

def test_delete_team(client: TestClient):
    # Create a team first
    create_response = client.post(
        "/api/teams",
        json={
            "name": "Manchester United",
            "city": "Manchester",
            "country": "England",
            "founded_year": "1878"
        }
    )
    team_id = create_response.json()["id"]
    
    # Delete the team
    response = client.delete(f"/api/teams/{team_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Team deleted successfully"
    
    # Verify team is deleted
    get_response = client.get(f"/api/teams/{team_id}")
    assert get_response.status_code == 404

def test_delete_team_not_found(client: TestClient):
    response = client.delete("/api/teams/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Team not found" 