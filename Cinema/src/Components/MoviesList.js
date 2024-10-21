// src/components/MoviesList.js
import React, { useEffect, useState } from 'react';
import { getMovies } from './moviesService';
import matrix from '../assets/matrix.jpg';
import inception from '../assets/inception.jpg';
import avengers from '../assets/avengers.jpg';
import batman from '../assets/batman.jpg';
import interstellar from '../assets/interstellar.jpg';
import avatar from '../assets/avatar.jpg';

const MoviesList = () => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchMovies = async () => {
      const moviesData = await getMovies();
      setMovies(moviesData);
    };

    fetchMovies();
  }, []);

  return (
    <div>
      <h1>Lista de Filmes</h1>
      <ul>
        {movies.map((movie) => (
          <li key={movie.id}>
            {movie.title} - {movie.genre} - {movie.rating}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MoviesList;
