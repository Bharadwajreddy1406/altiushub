import { createContext, useContext, useReducer, useEffect } from 'react';

const TaskContext = createContext();

const taskReducer = (state, action) => {
  switch (action.type) {
    case 'LOAD_TASKS':
      return action.payload;
    
    case 'ADD_TASK':
      return [...state, action.payload];
    
    case 'EDIT_TASK':
      return state.map(task => 
        task.id === action.payload.id ? action.payload : task
      );
    
    case 'DELETE_TASK':
      return state.filter(task => task.id !== action.payload);
    
    case 'TOGGLE_TASK':
      return state.map(task => 
        task.id === action.payload 
          ? { ...task, completed: !task.completed }
          : task
      );
    
    default:
      return state;
  }
};

export const TaskProvider = ({ children }) => {
  const [tasks, dispatch] = useReducer(taskReducer, []);

  useEffect(() => {
    const storedTasks = localStorage.getItem('tasks');
    if (storedTasks) {
      dispatch({ type: 'LOAD_TASKS', payload: JSON.parse(storedTasks) });
    }
  }, []);

  useEffect(() => {
    localStorage.setItem('tasks', JSON.stringify(tasks));
  }, [tasks]);

  
  const addTask = (title) => {
    const newTask = {
      id: Date.now().toString(),
      title: title.trim(),
      completed: false,
      createdAt: new Date().toISOString()
    };
    dispatch({ type: 'ADD_TASK', payload: newTask });
  };

  const editTask = (id, title) => {
    const taskToEdit = tasks.find(task => task.id === id);
    if (taskToEdit) {
      const updatedTask = {
        ...taskToEdit,
        title: title.trim(),
        updatedAt: new Date().toLocaleDateString()
      };
      dispatch({ type: 'EDIT_TASK', payload: updatedTask });
    }
  };

  const deleteTask = (id) => {
    dispatch({ type: 'DELETE_TASK', payload: id });
  };

  const toggleTask = (id) => {
    dispatch({ type: 'TOGGLE_TASK', payload: id });
  };

  const value = {
    tasks,
    addTask,
    editTask,
    deleteTask,
    toggleTask
  };

  return (
    <TaskContext.Provider value={value}>
      {children}
    </TaskContext.Provider>
  );
};

export const useTask = () => {
  const context = useContext(TaskContext);
  if (!context) {
    throw new Error('useTask must be used within a TaskProvider');
  }
  return context;
};
