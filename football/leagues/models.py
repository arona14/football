from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class League(SQLModel, table=True):
    __tablename__ = "leagues"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    logo: Optional[str] = None
    founded: Optional[str] = None
    type: Optional[str] = None
    level: Optional[int] = None
    country_name: Optional[str] = None
    country_code: Optional[str] = None
    country_flag: Optional[str] = None
    teams: list["Team"] = Relationship(back_populates="league")
