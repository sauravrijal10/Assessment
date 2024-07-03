# FastAPI Pokémon Project

## Project Description

This project is a REST API built with FastAPI that serves a list of Pokémon. The API fetches data from the [PokeAPI](https://pokeapi.co/) once and stores it in a PostgreSQL database. Subsequent requests are served from the database.

## Features

- List Pokémon with their name, image, and type
- Filter Pokémon by name and type
- Asynchronous database interactions using SQLAlchemy and asyncpg
- API versioning

## Requirements

- Docker
- Docker Compose

## Setup Instructions

### 1. Clone the repository 
   - To run application

      **sudo docker-compose up --build**

      Now you can go inside the docker container and run script.py to fetch data from the given endpoint

      **python3 script.py**

      After data has been fetched to the database then data can accessed in the endpoint - http://localhost:8000/api/v1/pokemons

      And for data filter based on name and type params can be passed to the same endpoint. The two params are name and type
