import React from 'react';
import Movies from './Components/Movies';
import SessionCarousel from './Components/SessionCarousel';
import './App.css';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>CineLux</h1> {/* Nome do site */}
            </header>
            <SessionCarousel />
            <Movies />
        </div>
    );
}

export default App;

