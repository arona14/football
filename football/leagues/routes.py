from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from football.database import get_session
from football.leagues.models import League
from football.leagues.schemas import LeagueCreate, LeagueRead, LeagueUpdate


league_router = APIRouter()


@league_router.get("/leagues", response_model=list[LeagueRead])
def get_leagues(session: Session = Depends(get_session)):
    """
    Get all leagues.
    """
    leagues = session.exec(select(League)).all()
    return leagues


@league_router.get("/leagues/{league_id}", response_model=LeagueRead)
def get_league(league_id: int, session: Session = Depends(get_session)):
    """
    Get a league by ID.
    """
    league = session.get(League, league_id)
    if not league:
        raise HTTPException(status_code=404, detail="League not found")
    return league


@league_router.post("/leagues", response_model=LeagueRead)
def create_league(league: LeagueCreate, session: Session = Depends(get_session)):
    """
    Create a new league.
    """
    existing_league = session.exec(
        select(League).where(League.name == league.name and League.country_name == league.country_name)
    ).first()
    
    if existing_league:
        raise HTTPException(
            status_code=400,
            detail="League already exists"
        )
    db_league = League.model_validate(league)
    session.add(db_league)
    session.commit()
    session.refresh(db_league)
    return db_league


@league_router.put("/leagues/{league_id}", response_model=LeagueRead)
def update_league(league_id: int, league: LeagueUpdate, session: Session = Depends(get_session)):
    """
    Update a league by ID.
    """
    db_league = session.get(League, league_id)
    if not db_league:
        raise HTTPException(status_code=404, detail="League not found")
    league.id = league_id
    session.merge(league)
    session.commit()
    session.refresh(league)
    return league


@league_router.delete("/leagues/{league_id}")
def delete_league(league_id: int, session: Session = Depends(get_session)):
    """
    Delete a league by ID.
    """
    league = session.get(League, league_id)
    if not league:
        raise HTTPException(status_code=404, detail="League not found")
    session.delete(league)
    session.commit()
    return {"detail": "League deleted"}
