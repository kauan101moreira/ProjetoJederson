import React, { useEffect, useState } from 'react';
import api from '../api'; // Importa o cliente Axios configurado
import matrix from '../assets/matrix.jpg';
import inception from '../assets/inception.jpg';
import avengers from '../assets/avengers.jpg';
import batman from '../assets/batman.jpg';
import interstellar from '../assets/interstellar.jpg';
import avatar from '../assets/avatar.jpg';
import toyStory from '../assets/toystory.jpg'
 
function Movies() {
    const [backendMovies, setBackendMovies] = useState([]); // Estado para armazenar filmes do backend

    // Lista estática de filmes
    const staticMovies = [
        {
            title: "Matrix",
            duration: "136 min",
            genre: "Ficção Científica",
            year: 1999,
            img: matrix,
            trailerUrl: "https://www.youtube.com/watch?v=mPYfd6PCmYY",
            wikipediaUrl: "https://pt.wikipedia.org/wiki/Matrix",
        },
        {
            title: "Inception",
            duration: "148 min",
            genre: "Ação, Ficção Científica",
            year: 2010,
            img: inception,
            trailerUrl: "https://www.youtube.com/watch?v=R_VX0e0PX90",
            wikipediaUrl: "https://pt.wikipedia.org/wiki/A_Origem",
        },
        {
            title: "Avengers",
            duration: "143 min",
            genre: "Ação, Super-heróis",
            year: 2012,
            img: avengers,
            trailerUrl: "https://www.youtube.com/watch?v=KeNEGtsCWEk",
            wikipediaUrl: "https://pt.wikipedia.org/wiki/The_Avengers_(2012)",
        },
        {
            title: "Batman",
            duration: "155 min",
            genre: "Ação, Aventura",
            year: 2022,
            img: batman,
            trailerUrl: "https://www.youtube.com/watch?v=HJv4LQxbVEA",
            wikipediaUrl: "https://pt.wikipedia.org/wiki/The_Batman_(filme)",
        },
        {
            title: "Interstellar",
            duration: "169 min",
            genre: "Ficção Científica",
            year: 2014,
            img: interstellar,
            trailerUrl: "https://www.youtube.com/watch?v=i6avfCqKcQo",
            wikipediaUrl: "https://pt.wikipedia.org/wiki/Interstellar",
        },
        {
            title: "Avatar 2",
            duration: "192 min",
            genre: "Ficção Científica, Aventura",
            year: 2022,
            img: avatar,
            trailerUrl: "https://www.youtube.com/watch?v=x5pZI-DmtrE",
            wikipediaUrl: "https://pt.wikipedia.org/wiki/Avatar:_O_Caminho_da_%C3%81gua",
        },
    ];

    useEffect(() => {
        const fetchBackendMovies = async () => {
            try {
                const response = await api.get('/movies'); // Requisição GET para o endpoint /movies
                setBackendMovies(response.data); // Armazena os filmes do backend no estado
            } catch (error) {
                console.error('Erro ao buscar filmes do backend:', error);
            }
        };
        fetchBackendMovies();
    }, []);
 
    const handleTrailerClick = (url) => {
        window.open(url, '_blank');
    };
 
    const handleWikipediaClick = (url) => {
        window.open(url, '_blank');
    };
 
    return (
        <div className="movies-list">
            {/* Exibe os filmes estáticos */}
            {staticMovies.map((movie, index) => (
                <div key={`static-${index}`} className="movie-card">
                    <img
                        src={movie.img}
                        alt={movie.title}
                        className="movie-cover"
                        onClick={() => handleTrailerClick(movie.trailerUrl)}
                        style={{ cursor: 'pointer' }}
                    />
                    <h3>{movie.title}</h3>
                    <p>
                        {movie.duration}, {movie.genre}, {movie.year}
                    </p>
                    <button
                        className="primary"
                        onClick={() => handleTrailerClick(movie.trailerUrl)}
                    >
                        Assistir Trailer
                    </button>
                    <button className="secondary"
                        onClick={() => handleWikipediaClick(movie.wikipediaUrl)}
                    >
                        Mais Informações
                    </button>
                </div>
            ))}

            {/* Exibe os filmes do backend */}
            {backendMovies.map((movie, index) => (
                <div key={`backend-${index}`} className="movie-card">
                    <img
                        src={movie.img || toyStory}  // Usando a imagem do backend ou uma imagem padrão
                        alt={movie.title}
                        className="movie-cover"
                        onClick={() => handleTrailerClick(movie.trailerUrl)}
                        style={{ cursor: 'pointer' }}
                    />
                    <h3>{movie.title}</h3>
                    <p>
                        {movie.duration} min, {movie.genre}, {movie.year}
                    </p>
                    <button
                        className="primary"
                        onClick={() => handleTrailerClick(movie.trailerUrl)}
                    >
                        Assistir Trailer
                    </button>
                    <button
                        className="secondary"
                        onClick={() => handleWikipediaClick(movie.trailerUrl)}
                    >
                        Mais Informações
                    </button>
                </div>
            ))}
        </div>
    );
};
 
export default Movies;