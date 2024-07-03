import asyncio
import aiohttp
from app.db import engine, Base, get_db
from app.crud import create_pokemon

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon?limit=100"  #To fetch only 100 data i have set limit in emdpoint

async def fetch_pokemons():
    async with aiohttp.ClientSession() as session:
        async with session.get(POKEAPI_URL) as response:
            data = await response.json()
            return data['results']

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    pokemons = await fetch_pokemons()
    
    async for db in get_db():
        for poke in pokemons:
            async with aiohttp.ClientSession() as session:
                async with session.get(poke['url']) as response:
                    poke_data = await response.json()
                    name = poke_data['name']
                    image = poke_data['sprites']['front_default']
                    types = ', '.join([t['type']['name'] for t in poke_data['types']])
                    await create_pokemon(db, name, image, types)

if __name__ == '__main__':
    asyncio.run(main())
