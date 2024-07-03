from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import get_pokemons
from app.db import get_db

router = APIRouter()

@router.get("/pokemons")
async def read_pokemons(type: str = None, name: str = None, db: AsyncSession = Depends(get_db)):
    pokemons = await get_pokemons(db)
    if type:
        pokemons = [pokemon for pokemon in pokemons if type in pokemon.type]
    if name:
        pokemons = [pokemon for pokemon in pokemons if name.lower() in pokemon.name.lower()]
    return pokemons
