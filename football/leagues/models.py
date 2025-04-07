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

    def __repr__(self):
        return f"League(id={self.id}, name={self.name}, country_id={self.country_id}, logo={self.logo}, founded={self.founded}, type={self.type}, level={self.level}, country_name={self.country_name}, country_code={self.country_code}, country_flag={self.country_flag})"
    
    def __str__(self):
        return f"League: {self.name}, Country ID: {self.country_id}, Logo: {self.logo}, Founded: {self.founded}, Type: {self.type}, Level: {self.level}, Country Name: {self.country_name}, Country Code: {self.country_code}, Country Flag: {self.country_flag}"
