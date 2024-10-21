// moviesService.js
const API_URL = 'http://localhost:8000/movies'; // URL do seu backend

export const getMovies = async () => {
    const response = await fetch(API_URL);
    if (!response.ok) {
        throw new Error('Erro ao buscar filmes');
    }
    return await response.json();
};

