from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from football.leagues.models import League


class Team(SQLModel, table=True):
    __tablename__ = "teams"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    city: str
    stadium: str
    league_id: Optional[int] = Field(default=None, foreign_key="leagues.id")
    league: Optional[League] = Relationship(back_populates="teams")
    founded_year: str
    manager: str
    championships_won: int
    players: list["Player"] = Relationship(back_populates="team")

    def __repr__(self):
        return f"Team(id={self.id}, name={self.name}, city={self.city}, stadium={self.stadium}, league={self.league}, founded_year={self.founded_year}, manager={self.manager}, players_count={self.players_count}, championships_won={self.championships_won})"
    def __str__(self):
        return f"Team: {self.name}, City: {self.city}, Stadium: {self.stadium}, League: {self.league}, Founded Year: {self.founded_year}, Manager: {self.manager}, Players Count: {self.players_count}, Championships Won: {self.championships_won}"