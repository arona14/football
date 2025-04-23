from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from football.database import get_session
from football.players.models import Player
from football.players.schemas import PlayerCreate, PlayerRead, PlayerUpdate


player_router = APIRouter()


@player_router.get("/players", response_model=List[PlayerRead])
def get_players(session: Session = Depends(get_session)):
    """
    Get all players.
    """
    players = session.exec(select(Player)).all()
    return players


@player_router.get("/players/{player_id}", response_model=PlayerRead)
def get_player(player_id: int, session: Session = Depends(get_session)):
    """
    Get a player by ID.
    """
    player = session.get(Player, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@player_router.post("/players", response_model=PlayerRead)
def create_player(player: PlayerCreate, session: Session = Depends(get_session)):
    """
    Create a new player.
    """
    existing_player = session.exec(
        select(Player).where(Player.first_name == player.first_name and Player.last_name == player.last_name
                             and Player.nationality == player.nationality)
    ).first()
    print("existing player:", existing_player)
    if existing_player:
        raise HTTPException(
            status_code=400,
            detail="Player already exists"
        )
    db_player = Player.model_validate(player)
    session.add(db_player)
    session.commit()
    session.refresh(db_player)
    return db_player


@player_router.put("/players/{player_id}", response_model=PlayerRead)
def update_player(player_id: int, player_update: PlayerUpdate, session: Session = Depends(get_session)):
    """
    Update a player by ID.
    """
    db_player = session.get(Player, player_id)
    if not db_player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    # Update only the fields that are provided in the update request
    player_data = player_update.model_dump(exclude_unset=True)
    for key, value in player_data.items():
        setattr(db_player, key, value)
    
    session.add(db_player)
    session.commit()
    session.refresh(db_player)
    return db_player


@player_router.delete("/players/{player_id}")
def delete_player(player_id: int, session: Session = Depends(get_session)):
    """
    Delete a player by ID.
    """
    db_player = session.get(Player, player_id)
    if not db_player:
        raise HTTPException(status_code=404, detail="Player not found")
    session.delete(db_player)
    session.commit()
    return {"detail": "Player deleted successfully"}
