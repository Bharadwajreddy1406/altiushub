import { useState } from "react";
import { useTask } from "../context/TaskContext";
import { Pencil, Trash2, } from "lucide-react";
import { Link } from "react-router-dom";

export const ShowTask = () => {
  const { tasks, editTask, deleteTask, toggleTask } = useTask();
  const [filter, setFilter] = useState("all");
  const [editingId, setEditingId] = useState(null);
  const [editingTitle, setEditingTitle] = useState("");

  const filteredTasks = tasks.filter((task) => {
    if (filter === "active") return !task.completed;
    if (filter === "completed") return task.completed;
    return true;
  });

  const totalTasks = tasks.length;
  const completedTasks = tasks.filter((task) => task.completed).length;
  const activeTasks = totalTasks - completedTasks;

  const handleEdit = (task) => {
    setEditingId(task.id);
    setEditingTitle(task.title);
  };

  const handleSaveEdit = (id) => {
    if (editingTitle.trim() && editingTitle.trim().length >= 3) {
      editTask(id, editingTitle);
      setEditingId(null);
      setEditingTitle("");
    } else {
      alert("Task title must be at least 3 characters long");
    }
  };

  const handleCancelEdit = () => {
    setEditingId(null);
    setEditingTitle("");
  };

  const handleDelete = (id, title) => {
    if (window.confirm(`Are you sure you want to delete "${title}"?`)) {
      deleteTask(id);
    }
  };

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString();
  };

  return (
    <div className="max-w-4xl mx-auto">
     

      <div className="space-y-4">
        {filteredTasks.length === 0 ? (
          <div className="bg-white rounded-lg shadow-md p-8 text-center">
        
            <h3 className="text-xl font-semibold text-gray-600 mb-2">
              {filter === "all"
                ? "No tasks yet"
                : filter === "active"
                ? "No active tasks"
                : "No completed tasks"}
            </h3>
            <p className="text-gray-500 mb-4">
              {filter === "all"
                ? "Create your first task to get started!"
                : filter === "active"
                ? "All tasks are completed!"
                : "No completed tasks yet."}
            </p>
            {filter === "all" && (
              <Link
                to="/add"
                className="inline-block bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors duration-200"
              >
                Create Your First Task
              </Link>
            )}
          </div>
        ) : (
          filteredTasks.map((task) => (
            <div
              key={task.id}
              className={`bg-white rounded-lg shadow-md p-4  transition-all duration-200 ${
                task.completed
                  ? "border-green-500 bg-green-500"
                  : "border-blue-500 hover:shadow-lg"
              }`}
            >
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3 flex-1">
                  <input
                    type="checkbox"
                    checked={task.completed}
                    onChange={() => toggleTask(task.id)}
                    className="w-5 h-5 text-blue-600 rounded"
                  />

                  {editingId === task.id ? (
                    <div className="flex-1 flex gap-2">
                      <input
                        type="text"
                        value={editingTitle}
                        onChange={(e) => setEditingTitle(e.target.value)}
                        className="flex-1 px-3 py-1 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                        autoFocus
                      />
                      <button
                        onClick={() => handleSaveEdit(task.id)}
                        className="px-3 py-1 bg-green-600 text-white rounded hover:bg-green-700"
                      >
                        ✓
                      </button>
                      <button
                        onClick={handleCancelEdit}
                        className="px-3 py-1 bg-gray-400 text-white rounded hover:bg-gray-500"
                      >
                        ✗
                      </button>
                    </div>
                  ) : (
                    <div className="flex-1">
                      <h3
                        className={`text-lg font-medium ${
                          task.completed
                            ? "text-gray-500 line-through"
                            : "text-gray-800"
                        }`}
                      >
                        {task.title}
                      </h3>
                      <p className="text-sm text-gray-500">
                        Created: {formatDate(task.createdAt)}
                        {task.updatedAt && (
                          <span> Updated: {formatDate(task.updatedAt)}</span>
                        )}
                      </p>
                    </div>
                  )}
                </div>

                {editingId !== task.id && (
                  <div className="flex gap-2">
                    <button
                      onClick={() => handleEdit(task)}
                      className="px-3 py-1 text-blue-600 hover:bg-blue-100 rounded "
                      title="Edit task"
                    >
                      <Pencil />
                    </button>
                    <button
                      onClick={() => handleDelete(task.id, task.title)}
                      className="px-3 py-1 text-red-600 hover:bg-red-100 rounded"
                      title="Delete task"
                    >
                      <Trash2 />
                    </button>
                  </div>
                )}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};
