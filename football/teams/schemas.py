from typing import Optional, List
from sqlmodel import SQLModel, Field
from football.teams.models import Team
from football.players.models import Player
from football.leagues.models import League


class TeamBase(SQLModel):
    name: str
    city: Optional[str] = None
    country: Optional[str] = None
    stadium: Optional[str] = None
    founded_year: Optional[str] = None
    manager: Optional[str] = None
    championships_won: Optional[int] = 0

class TeamCreate(TeamBase, table=False):
    league_id: Optional[int] = None


class TeamRead(TeamBase, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    players: List[Player] = []
    league: Optional[League] = None
    def __repr__(self):
        return f"Team(id={self.id}, name={self.name}, city={self.city}, stadium={self.stadium}, league={self.league}, founded_year={self.founded_year}, manager={self.manager}, players_count={self.players_count}, championships_won={self.championships_won})"

class TeamUpdate(SQLModel, table=False):
    name: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    stadium: Optional[str] = None
    founded_year: Optional[str] = None
    manager: Optional[str] = None
    championships_won: Optional[int] = None
    league_id: Optional[int] = None
