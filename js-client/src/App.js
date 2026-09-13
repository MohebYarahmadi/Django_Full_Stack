import React from "react";
import { Route, Routes } from "react-router-dom";
import ProtectedRoute from "./routers/ProtectedRoute";
import Home from "./pages/Home";
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <Routes>
        <Route path="/" element={
            <ProtectedRoute>
                <Home />
            </ProtectedRoute>
        } />
        <Route path="/login/" element={<div>Login</div>} />
    </Routes>
  );
}

export default App;
