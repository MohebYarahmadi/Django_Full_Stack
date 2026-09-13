import React from "react";
import { Navigate } from "react-router-dom";

// import { getUser } from "../hooks/user.actions";

function ProtectedRoute({ children }) {
  const { user} =
    JSON.parse(localStorage.getItem("auth"));
  return auth.account ? <>{children}</> : <Navigate to="/login/" />;
}

export default ProtectedRoute;
