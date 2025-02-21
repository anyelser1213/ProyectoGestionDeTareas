import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import './estilos.css';

function LoginForm({ onLogin }) {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({ email: '', password: '' });
    const [message, setMessage] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);

        try {
            const response = await fetch('http://127.0.0.1:8000/auth/token/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            if (response.ok) {
                const data = await response.json();
                localStorage.setItem('access_token', data.access);
                localStorage.setItem('refresh_token', data.refresh);

                onLogin();

                setMessage('Inicio de sesión exitoso');
                setTimeout(() => {
                    setMessage('');
                    navigate('/tareas');
                }, 1000);

            } else {
                const data = await response.json();
                if (response.status === 401) {
                    setMessage('Credenciales inválidas');
                } else if (response.status === 404) {
                    setMessage('Usuario no encontrado');
                } else {
                    setMessage(data.detail || 'Error en el inicio de sesión');
                }
                setTimeout(() => setMessage(''), 3000);
            }
        } catch (error) {
            setMessage('Error de conexión');
            setTimeout(() => setMessage(''), 3000);
            console.error("Error en la petición:", error);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="login-form">
            <h2>Iniciar Sesión</h2>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label>Correo electrónico:</label>
                    <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleInputChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label>Contraseña:</label>
                    <input
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleInputChange}
                        required
                    />
                </div>

                <button type="submit" disabled={isLoading}>
                    {isLoading ? 'Cargando...' : 'Iniciar Sesión'}
                </button>
            </form>

            {message && <p className="message">{message}</p>}

            <Link to="/registroUsuario"> {/* Enlace a la página de registro */}
                <button className="button2" type="button2">Registrarse</button>
            </Link>
        </div>
    );
}

export default LoginForm;