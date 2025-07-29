import React from "react";
import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";
import UserPage from "../pages/UserPage";

const AppRouter = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/user/:id" element={<UserPage />} />
        <Route path="*" element={<Navigate to="/user/2" />} />
      </Routes>
    </BrowserRouter>
  );
};

export default AppRouter;
