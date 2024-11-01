import React, { useEffect, useState } from 'react';
import { getMovies } from './moviesService'; // Certifique-se de que o caminho para o serviço está correto

import matrix from '../assets/matrix.jpg';
import inception from '../assets/inception.jpg';
import avengers from '../assets/avengers.jpg';
import batman from '../assets/batman.jpg'; // Caminho da imagem do Batman
import interstellar from '../assets/interstellar.jpg'; // Caminho da imagem de Interstellar
import avatar from '../assets/avatar.jpg'; // Caminho da imagem de Avatar

const Movies = () => {
    const [movies, setMovies] = useState([]); // Estado para armazenar os filmes
    const [loading, setLoading] = useState(true); // Estado para controle de loading

    useEffect(() => {
        const fetchMovies = async () => {
            try {
                const moviesData = await getMovies(); // Chama o serviço para obter os filmes
                setMovies(moviesData); // Armazena os filmes no estado
            } catch (error) {
                console.error("Erro ao buscar filmes:", error);
            } finally {
                setLoading(false); // Define loading como false após a requisição
            }
        };

        fetchMovies();
    }, []); // Executa o efeito apenas uma vez quando o componente é montado

    if (loading) {
        return <div>Loading...</div>; // Exibe uma mensagem de loading
    }

    return (
        <div className="movies-list">
            {movies.map((movie) => (
                <div key={movie.id} className="movie-card">
                    <img src={movie.img} alt={movie.title} className="movie-cover" />
                    <h3>{movie.title}</h3>
                    <p>{movie.duration}, {movie.genre}, {movie.year}</p>
                    <button className="primary">Assistir Trailer</button>
                    <button className="secondary">Mais Informações</button>
                </div>
            ))}
        </div>
    );
};

export default Movies;
