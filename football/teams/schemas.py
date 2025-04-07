from typing import Optional, List
from sqlmodel import SQLModel, Field
from football.teams.models import Team
from football.players.models import Player
from football.leagues.models import League


class TeamBase(SQLModel):
    name: str
    city: str
    stadium: str
    founded_year: str
    manager: str
    championships_won: int

class TeamCreate(TeamBase, table=False):
    league_id: Optional[int] = None


class TeamRead(TeamBase, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    players: List[Player] = []
    league: League = None
    def __repr__(self):
        return f"Team(id={self.id}, name={self.name}, city={self.city}, stadium={self.stadium}, league={self.league}, founded_year={self.founded_year}, manager={self.manager}, players_count={self.players_count}, championships_won={self.championships_won})"

class TeamUpdate(TeamBase, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    league_id: Optional[int] = None
