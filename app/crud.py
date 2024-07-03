from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Pokemon

async def get_pokemons(db: AsyncSession):
    result = await db.execute(select(Pokemon))
    return result.scalars().all()

async def create_pokemon(db: AsyncSession, name: str, image: str, type: str):
    pokemon = Pokemon(name=name, image=image, type=type)
    db.add(pokemon)
    await db.commit()
    await db.refresh(pokemon)
    return pokemon
