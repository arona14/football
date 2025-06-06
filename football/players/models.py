from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Player(SQLModel, table=True):
    __tablename__ = "players"

    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    age: int
    nationality: str
    position: str
    height: Optional[int] = None
    weight: Optional[int] = None
    foot: Optional[str] = None
    number: Optional[int] = None
    image: Optional[str] = None
    date_of_birth: Optional[str] = None
    market_value: Optional[str] = None
    team_id: Optional[int] = Field(default=None, foreign_key="teams.id")
    team: Optional["Team"] = Relationship(back_populates="players")
