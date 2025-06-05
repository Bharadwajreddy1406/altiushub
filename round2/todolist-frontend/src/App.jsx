import { Route, Routes } from "react-router-dom";
import "./App.css";
import AddTask from "./components/AddTask";
import { Navbar } from "./components/NavBar";
import { ShowTask } from "./components/ShowTask";
import { TaskProvider } from "./context/TaskContext";

function App() {
  return (
    <TaskProvider>
      <div className="bg-slate-50">
        <Navbar/>
        <main className="container mx-auto px-4 py-8">
          <Routes>
            <Route path="/" element={<ShowTask/>} />
            <Route path="/add" element={<AddTask/>} />
            <Route path="/tasks" element={<ShowTask/>} />
          </Routes>
        </main>
      </div>
    </TaskProvider>
  );
}

export default App;
