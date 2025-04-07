from fastapi import FastAPI

from football.database import  create_db_and_tables
from football.players.routes import player_router
from football.teams.routes import team_router
from football.leagues.routes import league_router
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(debug=True)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    print("Database and tables created.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(player_router, prefix="/api", tags=["players"])
app.include_router(team_router, prefix="/api", tags=["teams"])
app.include_router(league_router, prefix="/api", tags=["leagues"])
