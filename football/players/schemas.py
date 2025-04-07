from typing import Optional
from sqlmodel import SQLModel, Field
from football.teams.schemas import TeamRead


class PlayerBase(SQLModel):
    firt_name: str
    last_name: str
    age: int
    nationality: str
    position: str
    country_id: int
    height: Optional[int] = None
    weight: Optional[int] = None
    foot: Optional[str] = None
    number: Optional[int] = None
    image: Optional[str] = None
    date_of_birth: Optional[str] = None
    market_value: Optional[str] = None
    team_id: Optional[int] = None

class PlayerCreate(PlayerBase, table=False):
    pass


class PlayerRead(PlayerBase, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    team: Optional["TeamRead"] = None

class PlayerUpdate(SQLModel, table=False):
    pass
