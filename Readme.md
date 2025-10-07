# PokeAPI Data Analysis App

This Flask-based web application fetches and analyzes data from the [PokeAPI](https://pokeapi.co/), providing insights into various Pokémon characteristics. The app includes user authentication, database storage, analytical views, and data visualizations.

---

##  Technologies and Tools

- **Python 3.10**
- **Flask** – web framework (MVC)
- **Flask-SQLAlchemy** – ORM for PostgreSQL
- **Flask-Migrate** – migrations
- **Flask-JWT-Extended** – JWT-based auth
- **PostgreSQL** – relational database
- **Docker + Docker Compose** – containerization
- **PokeAPI** – external REST API source
- **Chart.js** – frontend data visualizations

---

##  Features

-  **JWT User Authentication** (register/login)
-  **Fetch Pokémon Data** 
-  **Analytical Views**:
  - Average HP, Attack, Defense by Type
  - Top Pokémon by combined stats
  - Average Experience per Type
  - Tallest and Heaviest Pokémon per Type
  - Type Distribution (count)
  - Stat Range Comparisons by Type
-  **Chart Visualizations** using Chart.js
-  **Dockerized** PostgreSQL + Flask stack

---

##  Project Structure

```
poke_api_app/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── services/
│   │   ├── date_fetcher.py
│   │   └── analysis.py
│   └── templates/
│       ├── index.html
│       ├── analysis.html
│       └── charts.html
├── run.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/byienio/poke_api_app.git
cd poke_api_app
```
### 2. Start with Docker
```bash
docker-compose up --build
```
### 3. Apply migration to database in web container exec
```
flask db upgrade
```
### 4. Register account via Postman
```
Method POST
http://127.0.0.1:5000/register
body - raw json
example:
{
    "username": "user",
    "password": "user"
}
```
### 5. Login with created account via Postman
```
Method POST
http://127.0.0.1:5000/login
body - raw json
example:
{
    "username": "user",
    "password": "user"
}
copy your token
```
### 6. Fetch data via Postman
```
Method GET
http://127.0.0.1:5000/fetch-pokemon
Authorization - Bearer token <- copy here your token from login
```
### 7. Access the App

Visit: [http://localhost:5000](http://localhost:5000)

---

##  API Endpoints

### Authentication

- `POST /register`: Register with `username` and `password`
- `POST /login`: Login and get JWT

### Data & Analysis

- `GET /fetch-pokemon`: Fetch/store Pokémon data (JWT required)
- `GET /analysis/type-summary`: Stats by Pokémon type
- `GET /analysis/top-overall`: Top Pokémon by stats
- `GET /analysis/experience-by-type`: Avg EXP per type
- `GET /analysis/tallest-heaviest`: Extremes by type
- `GET /analysis/type-distribution`: Type count
- `GET /analysis/stat-range`: Stat range by type
- `GET /charts`: Data visualizations (Chart.js)
- `GET /`: Landing page

---

## Environment Variables (Docker Compose defaults)

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=poke_db
FLASK_ENV=development
JWT_SECRET_KEY=super-secret
```

---

##  License

MIT License

---

##  Acknowledgements

- [PokeAPI](https://pokeapi.co/) for Pokémon data
- [Chart.js](https://www.chartjs.org/) for charting
- Flask + SQLAlchemy for backend structure
