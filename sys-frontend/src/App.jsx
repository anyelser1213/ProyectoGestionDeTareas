import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './componentes/LOGIN/Login';
import Inicio from './componentes/INICIO/Inicio';
import Todo from './componentes/TAREAS/Tareas';
import Contacto from './componentes/CONTACTO/Contacto';
import RegistroUsuarios from './componentes/USUARIOS/Registro';
import Tareas from './componentes/TAREAS/Tareas';

function App() {
    const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem('access_token')); // Usa solo isAuthenticated

    useEffect(() => {
        // Esta función se llama cuando el componente se monta y cada vez que cambia localStorage
        const checkAuth = () => {
            setIsAuthenticated(!!localStorage.getItem('access_token'));
        };

        // Escucha cambios en localStorage (incluyendo cuando se actualiza desde otro componente)
        window.addEventListener('storage', checkAuth);

        // También verifica la autenticación al montar el componente
        checkAuth();

        return () => {
            window.removeEventListener('storage', checkAuth);
        };
    }, []); // El array vacío asegura que se ejecuta solo una vez al montar y desmontar

    return (
        <Router>
            <Routes>
                <Route path="/login" element={!isAuthenticated ? <Login onLogin={() => setIsAuthenticated(true)} /> : <Navigate to="/tareas" />} /> {/* Pasa la función onLogin */}
                <Route path="/tareas" element={isAuthenticated ? <Tareas /> : <Navigate to="/login" />} />
                <Route path="/" element={isAuthenticated ? <Todo /> : <Navigate to="/login" />} />
                <Route path="/contacto" element={<Contacto />} />
                <Route path="/registroUsuario" element={<RegistroUsuarios />} />
                <Route path="*" element={<Navigate to="/login" />} />
            </Routes>
        </Router>
    );
}

export default App;
