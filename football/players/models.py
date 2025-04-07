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
    country_id: int
    height: Optional[int] = None
    weight: Optional[int] = None
    foot: Optional[str] = None
    number: Optional[int] = None
    image: Optional[str] = None
    date_of_birth: Optional[str] = None
    market_value: Optional[str] = None
    team_id: Optional[int] = Field(default=None, foreign_key="teams.id")
    team: Optional["Team"] = Relationship(back_populates="players")

    def __repr__(self):
        return f"Player(id={self.id}, name={self.name}, age={self.age}, nationality={self.nationality}, position={self.position}, team_id={self.team_id}, league_id={self.league_id}, height={self.height}, weight={self.weight}, foot={self.foot}, market_value={self.market_value})"
    
    def __str__(self):
        return f"Player: {self.name}, Age: {self.age}, Nationality: {self.nationality}, Position: {self.position}, Team ID: {self.team_id}, League ID: {self.league_id}, Height: {self.height}, Weight: {self.weight}, Foot: {self.foot}, Market Value: {self.market_value}"
