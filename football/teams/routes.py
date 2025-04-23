from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from football.database import get_session
from football.teams.models import Team
from football.teams.schemas import TeamCreate, TeamRead, TeamUpdate


team_router = APIRouter()


@team_router.get("/teams", response_model=List[TeamRead])
def get_teams(session: Session = Depends(get_session)):
    """
    Get all teams.
    """
    teams = session.exec(select(Team)).all()
    return teams


@team_router.get("/teams/{team_id}", response_model=TeamRead)
def get_team(team_id: int, session: Session = Depends(get_session)):
    """
    Get a team by ID.
    """
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@team_router.post("/teams", response_model=TeamRead)
def create_team(team: TeamCreate, session: Session = Depends(get_session)):
    """
    Create a new team.
    """
    existing_team = session.exec(
        select(Team).where(Team.name == team.name and Team.city == team.city)
    ).first()
    
    if existing_team:
        raise HTTPException(
            status_code=400,
            detail="Team already exists"
        )
    db_team = Team.model_validate(team)
    session.add(db_team)
    session.commit()
    session.refresh(db_team)
    return db_team


@team_router.put("/teams/{team_id}", response_model=TeamRead)
def update_team(team_id: int, team_update: TeamUpdate, session: Session = Depends(get_session)):
    """
    Update a team by ID.
    """
    db_team = session.get(Team, team_id)
    if not db_team:
        raise HTTPException(status_code=404, detail="Team not found")
    
    # Update only the fields that are provided in the update request
    team_data = team_update.model_dump(exclude_unset=True)
    for key, value in team_data.items():
        setattr(db_team, key, value)
    
    session.add(db_team)
    session.commit()
    session.refresh(db_team)
    return db_team


@team_router.delete("/teams/{team_id}")
def delete_team(team_id: int, session: Session = Depends(get_session)):
    """
    Delete a team by ID.
    """
    db_team = session.get(Team, team_id)
    if not db_team:
        raise HTTPException(status_code=404, detail="Team not found")
    session.delete(db_team)
    session.commit()
    return {"message": "Team deleted successfully"}
