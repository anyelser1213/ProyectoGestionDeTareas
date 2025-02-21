import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './css/registroUsuarios.css'; // Importa el archivo CSS

function RegistroFormUsuario() {

  // ... dentro de tu componente
  const navigate = useNavigate();
  
  // Estado para manejar los datos del formulario
  const [formData, setFormData] = useState({
    email: '',
    telefono: '',
    password: '',
  });

  // Estado para manejar errores de validación
  const [errors, setErrors] = useState({});

  // Función para manejar cambios en los campos del formulario
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  // Función para validar el formulario
  const validateForm = () => {
    const newErrors = {};

    if (!formData.email.trim()) {
      newErrors.email = 'El correo electrónico es obligatorio';
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = 'El correo electrónico no es válido';
    }

    // Validar el teléfono
    if (!formData.telefono.trim()) {
      newErrors.telefono = 'El teléfono es obligatorio';
    } else if (!/^\d+$/.test(formData.telefono)) {
      newErrors.telefono = 'El teléfono debe contener solo números';
    } else if (formData.telefono.length !== 10) {
      newErrors.telefono = 'El teléfono debe tener 10 dígitos';
    }

    if (!formData.password.trim()) {
      newErrors.password = 'La contraseña es obligatoria';
    } else if (formData.password.length < 6) {
      newErrors.password = 'La contraseña debe tener al menos 6 caracteres';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0; // Retorna true si no hay errores
  };

  // Función para manejar el envío del formulario
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (validateForm()) {
      try {
        // Enviar los datos a la API usando fetch
        const response = await fetch('http://127.0.0.1:8000/auth/users/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(formData),
          //{ "email": "carlos5@example.com", "telefono": "123456789", "password": "123"},
          /*JSON.stringify(formData),*/
        });

        if (response.ok) {
          // Si el registro es exitoso
          alert('Registro exitoso');
          setFormData({
            email: '',
            telefono: '',
            password: '',
          });
          setErrors({}); // Limpiar errores
          
          // Redirigir al login
          navigate('/login'); // Reemplaza '/login' con la ruta correcta a tu página de login

        } else {
          // Si hay un error en el registro
          const data = await response.json();
          if (data.email) {
            setErrors({ email: data.email[0] }); // Mostrar error de correo
          } else if (data.telefono) {
            setErrors({ telefono: data.telefono[0] }); // Mostrar error de teléfono
          } else {
            setErrors({ general: 'Error en el registro' }); // Error general
          }
        }
      } catch (error) {
        // Si hay un error de conexión
        setErrors({ general: 'Error de conexión'+error });
      }
    }
  };

  return (
    <div className="register-form">
      <h2>Registro de Usuario</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Correo electrónico:</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
          />
          {errors.email && <span className="error">{errors.email}</span>}
        </div>

        <div className="form-group">
          <label>Teléfono:</label>
          <input
            type="tel"
            name="telefono"
            value={formData.telefono}
            onChange={handleInputChange}
          />
          {errors.telefono && <span className="error">{errors.telefono}</span>}
        </div>

        <div className="form-group">
          <label>Contraseña:</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleInputChange}
          />
          {errors.password && <span className="error">{errors.password}</span>}
        </div>

        {errors.general && <span className="error">{errors.general}</span>}

        <button type="submit">Registrarse</button>
      </form>
    </div>
  );
}

export default RegistroFormUsuario;