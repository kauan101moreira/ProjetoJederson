from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.include_router(ratings.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Configuração CORS para permitir que o React acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite qualquer origem (ajuste conforme necessário)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock dos dados dos filmes
movies_data = [
    {"title": "Matrix", "duration": "136 min", "genre": "Ficção Científica", "year": 1999, "img": "/static/matrix.jpg"},
    {"title": "Inception", "duration": "148 min", "genre": "Ação, Ficção Científica", "year": 2010, "img": "/static/inception.jpg"},
    {"title": "Avengers", "duration": "143 min", "genre": "Ação, Super-heróis", "year": 2012, "img": "/static/avengers.jpg"},
    {"title": "Batman", "duration": "155 min", "genre": "Ação, Aventura", "year": 2005, "img": "/static/batman.jpg"},
    {"title": "Interstellar", "duration": "169 min", "genre": "Ficção Científica", "year": 2014, "img": "/static/interstellar.jpg"},
    {"title": "Avatar", "duration": "162 min", "genre": "Ficção Científica, Aventura", "year": 2009, "img": "/static/avatar.jpg"},
]

@app.get("/movies")
def get_movies():
    return {"movies": movies_data}

# Servir arquivos estáticos (imagens)
app.mount("/static", StaticFiles(directory="static"), name="static")
