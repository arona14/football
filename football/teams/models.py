from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from football.leagues.models import League


class Team(SQLModel, table=True):
    __tablename__ = "teams"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    city: Optional[str] = None
    country: Optional[str] = None
    stadium: Optional[str] = None
    league_id: Optional[int] = Field(default=None, foreign_key="leagues.id")
    league: Optional[League] = Relationship(back_populates="teams")
    founded_year: Optional[str] = None
    manager: Optional[str] = None
    championships_won: int
    players: list["Player"] = Relationship(back_populates="team")
