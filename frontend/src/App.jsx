import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodoTitle, setNewTodoTitle] = useState('');
  const [pop, setPop] = useState(false);

  // 🌍 Base Endpoint URL
  const API_URL = 'https://todo-backend-8q48.onrender.com/todos';

  // 🔄 FETCH ALL
  const fetchTodos = async () => {
    try {
      setPop(true)
      const response = await fetch(API_URL);
      const data = await response.json();
      setTodos(data);

    } catch (error) {
      console.error("Error connecting to backend:", error);
    }
    setPop(false);
  };

  useEffect(() => {
    fetchTodos();
  }, []);

  // ➕ CREATE
  const addTodo = async (e) => {
    e.preventDefault();
    if (!newTodoTitle.trim()) return;

    try {
      setPop(true)

      const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: newTodoTitle }),
      });

      if (response.ok) {
        setNewTodoTitle('');
        fetchTodos();
        setPop(false)
      }
    } catch (error) {
      console.error("Error adding todo:", error);
    }
  };

  // ☑️ TOGGLE STATUS (Appends /id explicitly to base path)
  const toggleTodo = async (id) => {
    setPop(true)
    try {
      const response = await fetch(`${API_URL}/${id}`, {
        method: 'PATCH',
      });

      if (response.ok) {
        fetchTodos();
      }
    } catch (error) {
      console.error("Error toggling todo:", error);
    }
    setPop(false)

  };

  // ❌ DELETE (Appends /id explicitly to base path)
  const deleteTodo = async (id) => {
    try {
      setPop(true);
      const response = await fetch(`${API_URL}/${id}`, {
        method: 'DELETE',
      });

      if (response.ok) {
        fetchTodos();
        setPop(false);
      }
    } catch (error) {
      console.error("Error deleting todo:", error);
    }
  };

  return (
    <div className="todo-container">

      <h1>Task Manager</h1>
      
      <form onSubmit={addTodo} className="todo-form">
        <input
          type="text"
          placeholder="Add a new task..."
          value={newTodoTitle}
          onChange={(e) => setNewTodoTitle(e.target.value)}
        />
        <button type="submit">Add</button>
      </form>

      <ul className="todo-list">
        {todos.map((todo) => (
          <li key={todo.id} className={todo.completed ? 'completed' : ''}>
            <span onClick={() => toggleTodo(todo.id)}>
              {todo.completed ? '✅' : '⬜'} {todo.title}
            </span>
            <button onClick={() => deleteTodo(todo.id)} className="delete-btn">
              Delete
            </button>
          </li>
        ))}
      </ul>
      {pop && (
        <div className="pop">Please wait... free databases are slow</div>
      )}
    </div>
  );
}

export default App;