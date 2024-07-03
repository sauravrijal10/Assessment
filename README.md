# FastAPI Pokemon API

## About Project
1. **In this project i have fetched and saved data in database from a specific endpoint with the help of script.py**
2. **Also user can get list of all the data from database in the endpoint - http://localhost:8000/api/v1/pokemons**
3. **To filter the data user can pass params to the above endpoint. Two params are type and name**


## Run the project
   First of all create a virtual env and install all the dependencies from requirements.txt which i have generate from pip freeze

   After all the dependencies are installed and virtual environment is activate you can run 

   **alembic upgrade head**

   for database migration and to run the application you can use the command below

   **uvicorn app.main:app --reload**
