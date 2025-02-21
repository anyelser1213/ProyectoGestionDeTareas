import React, { useState, useEffect } from "react";
import { jwtDecode } from 'jwt-decode';
import { useNavigate } from 'react-router-dom';
import './estilos.css';

function Tareas() {
    const [tasks, setTasks] = useState([]);
    const [task, setTask] = useState("");
    const [editingIndex, setEditingIndex] = useState(null);
    const [editingText, setEditingText] = useState("");
    const navigate = useNavigate();

    const token = localStorage.getItem('access_token');
    const decodedToken = jwtDecode(token);
    const userId = decodedToken.user_id;

    useEffect(() => {
        fetchTasks();
    }, []);

    const fetchTasks = async () => {
        try {
            const token = localStorage.getItem('access_token'); // Nombre consistente del token
            console.log("Token JWT:", token);
    
            const response = await fetch('http://127.0.0.1:8000/api/tareasUser/', {
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
            });
    
            console.log("Respuesta de la API:", response); // Verifica la respuesta
    
            if (response.ok) {
                console.log("Tareas obtenidas correctamente");
                const data = await response.json();
                console.log("Datos de las tareas:", data); // Verifica los datos
                setTasks(data);
            } else {
                console.error("Error al cargar tareas:", response.status);
                const errorData = await response.json(); // Intenta obtener detalles del error
                console.error("Detalles del error:", errorData);
    
                if (response.status === 401) {
                    console.log("Token inválido o expirado");
                    // Redirige al usuario a la página de inicio de sesión
                } else if (response.status === 403) {
                    console.log("No tienes permisos para acceder a este recurso");
                }
            }
        } catch (error) {
            console.error("Error al cargar tareas:", error);
        }
    };

    const addTask = async () => {
        
        try {
            

            if (task.trim()) {
                const response = await fetch('http://127.0.0.1:8000/api/tareas/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ titulo: task, completado: false, usuario: userId }),
                });

                if (response.ok) {
                    const newTask = await response.json();
                    setTasks([...tasks, newTask]);
                    setTask("");
                } else {
                    console.error("Error al agregar tarea:", response.status);
                    const errorData = await response.json();
                    console.error("Detalles del error:", errorData);
                }
            }
        } catch (error) {
            console.error("Error al decodificar o agregar tarea:", error);
        }
    };

    const toggleTask = async (index) => {
        const updatedTasks = [...tasks];
        updatedTasks[index].completado = !updatedTasks[index].completado;

        try {
            const response = await fetch(`http://127.0.0.1:8000/api/tareas/${updatedTasks[index].id}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(updatedTasks[index]),
            });

            if (response.ok) {
                setTasks(updatedTasks);
            } else {
                console.error("Error al actualizar tarea:", response.status);
            }
        } catch (error) {
            console.error("Error al actualizar tarea:", error);
        }
    };

    const startEditing = (index) => {
        setEditingIndex(index);
        setEditingText(tasks[index].titulo);
    };

    const saveEdit = async (index) => {
        const updatedTasks = [...tasks];
        updatedTasks[index].titulo = editingText;

        try {
            const response = await fetch(`http://127.0.0.1:8000/api/tareas/${updatedTasks[index].id}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(updatedTasks[index]),
            });

            if (response.ok) {
                setTasks(updatedTasks);
                setEditingIndex(null);
            } else {
                console.error("Error al guardar edición:", response.status);
            }
        } catch (error) {
            console.error("Error al guardar edición:", error);
        }
    };

    const deleteTask = async (index) => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/tareas/${tasks[index].id}/`, {
                method: 'DELETE',
            });
            if (response.ok) {
                setTasks(tasks.filter((_, i) => i !== index));
            } else {
                console.error("Error al eliminar tarea:", response.status);
            }
        } catch (error) {
            console.error("Error al eliminar tarea:", error);
        }
    };

    const handleLogout = async () => {
      try {
          const refreshToken = localStorage.getItem('refresh_token'); // Obtén el refresh token
  
          const response = await fetch('http://127.0.0.1:8000/api/logout/', { // URL de la vista de logout
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({ refresh_token: refreshToken }), // Envía el refresh token en el cuerpo
          });
  
          if (response.ok) {
              localStorage.removeItem('access_token');
              localStorage.removeItem('refresh_token'); // Elimina también el refresh token
              window.location.reload(); // Recarga la página
              //navigate('/login');
          } else {
              console.error("Error al cerrar sesión:", response.status);
          }
      } catch (error) {
          console.error("Error al cerrar sesión:", error);
      }
  };

    return (
        <div className="todo-app">
            <h1>Lista de Tareas</h1>
            <button className="logout-button" onClick={handleLogout}>Cerrar Sesión</button>

            <input
                type="text"
                value={task}
                onChange={(e) => setTask(e.target.value)}
                placeholder="Escribe una tarea..."
                onKeyDown={(e) => {
                    if (e.key === "Enter") {
                        addTask();
                    }
                }}
            />

            <button className="add-button" onClick={addTask}>
                Agregar
            </button>

            <ul>
                {tasks.map((t, index) => (
                    <li key={index}>
                        {editingIndex === index ? (
                            <>
                                <input
                                    type="text"
                                    value={editingText}
                                    onChange={(e) => setEditingText(e.target.value)}
                                />
                                <button
                                    className="action-button save-button"
                                    onClick={() => saveEdit(index)}
                                >
                                    Guardar
                                </button>
                            </>
                        ) : (
                            <>
                                <span
                                    className={`task-text ${t.completado ? "completed" : ""}`}
                                    onClick={() => toggleTask(index)}
                                >
                                    {t.titulo}
                                </span>
                                <div>
                                    <button
                                        className={`action-button complete-button ${t.completado ? "completed" : ""}`}
                                        onClick={() => toggleTask(index)}
                                    >
                                        {t.completado ? "✔️" : "✅"}
                                    </button>
                                    <button
                                        className="action-button edit-button"
                                        onClick={() => startEditing(index)}
                                    >
                                        ✏️
                                    </button>
                                    <button
                                        className="action-button delete-button"
                                        onClick={() => deleteTask(index)}
                                    >
                                        ❌
                                    </button>
                                </div>
                            </>
                        )}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Tareas;