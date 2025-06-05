import { useState } from 'react';
import { useTask } from '../context/TaskContext';
import { useNavigate } from 'react-router-dom';

const AddTask = () => {
    const [title, setTitle] = useState('');
    const [error, setError] = useState('');
    const { addTask } = useTask();
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        setError('');

        if (!title.trim()) {
            setError('Task title is required');
            return;
        }

        if (title.trim().length < 3) {
            setError('Task title must be at least 3 characters long');
            return;
        }

        addTask(title);
        setTitle('');
        
        alert('Task added successfully!');
        navigate('/');
    };

    return (
        <div className="bg-slate rounded-lg shadow-md p-6">
            <h2 className="text-2xl font-bold text-gray mb-6 text-center">
                Add New Task
            </h2>
            
            <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                    <label 
                        htmlFor="title" 
                        className="block text-sm font-medium text-gray mb-2"
                    >
                        Task Title
                    </label>
                    <input
                        type="text"
                        id="title"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        placeholder="Enter your task..."
                        className={`w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 ${
                            error ? 'border-red-500' : 'border-gray-300'
                        }`}
                    />
                    {error && (
                        <p className="text-red-300 text-sm mt-1">{error}</p>
                    )}
                </div>

                <div className="flex gap-3">
                    <button
                        type="submit"
                        className="flex-1 bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-colors duration-200"
                    >
                        Add Task
                    </button>
                    <button
                        type="button"
                        onClick={() => navigate('/')}
                        className="flex-1 bg-gray-300 text-gray-700 py-2 px-4 rounded-lg hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-500 transition-colors duration-200"
                    >
                        Cancel
                    </button>
                </div>
            </form>
        </div>
    );
};

export default AddTask;
