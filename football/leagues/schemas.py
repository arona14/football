from typing import Optional
from sqlmodel import SQLModel, Field
from football.teams.schemas import TeamRead


class LeagueBase(SQLModel):
    logo: Optional[str] = None
    founded: Optional[str] = None
    type: Optional[str] = None
    level: Optional[int] = None
    country_name: Optional[str] = None
    country_code: Optional[str] = None
    country_flag: Optional[str] = None


class LeagueCreate(LeagueBase, table=False):
    name: str
   

class LeagueRead(LeagueBase, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    teams: Optional[list["TeamRead"]] = None


class LeagueUpdate(LeagueBase, table=False):
    name: Optional[str] = None
