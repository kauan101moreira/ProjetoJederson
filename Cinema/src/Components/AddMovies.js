// AddMovie.js
import React, { useState } from 'react';
import api from '../api'; // Importa o cliente Axios configurado

// Define o componente AddMovie para o usuário adicionar filmes
const AddMovie = () => {
    const [title, setTitle] = useState('');
    const [genre, setGenre] = useState('');
    const [description, setDescription] = useState('');
    const [rating, setRating] = useState(0);
    const [year, setYear] = useState('');
    const [trailerUrl, setTrailerUrl] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const newMovie = { title, genre, description, rating, year, trailerUrl };
            await api.post('/movies', newMovie); // Requisição POST para o endpoint /movies
            alert('Filme adicionado com sucesso!');
            setTitle('');
            setGenre('');
            setDescription('');
            setRating(0);
            setYear('');
            setTrailerUrl('');
        } catch (error) {
            console.error('Erro ao adicionar filme:', error);
            alert('Erro ao adicionar filme.');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Adicionar Novo Filme</h2>
            <div>
                <label>Título:</label>
                <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} required />
            </div>
            <div>
                <label>Gênero:</label>
                <input type="text" value={genre} onChange={(e) => setGenre(e.target.value)} required />
            </div>
            <div>
                <label>Descrição:</label>
                <textarea value={description} onChange={(e) => setDescription(e.target.value)} required />
            </div>
            <div>
                <label>Classificação:</label>
                <input type="number" value={rating} onChange={(e) => setRating(parseFloat(e.target.value))} step="0.1" required />
            </div>
            <div>
                <label>Ano:</label>
                <input type="number" value={year} onChange={(e) => setYear(parseInt(e.target.value))} required />
            </div>
            <div>
                <label>URL do Trailer:</label>
                <input type="url" value={trailerUrl} onChange={(e) => setTrailerUrl(e.target.value)} required />
            </div>
            <button type="submit">Adicionar Filme</button>
        </form>
    );
};

export default AddMovie;
