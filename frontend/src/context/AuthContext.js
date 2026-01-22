'use client';

import React, { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAdmin, setIsAdmin] = useState(false);
  const api_url = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

  const checkAuth = async () => {
    try {
      // We use withCredentials to send session cookies to Django
      const res = await axios.get(`${api_url}/user-status/`, { withCredentials: true });
      setIsAdmin(res.data.is_staff);
    } catch (err) {
      setIsAdmin(false);
    }
  };

  useEffect(() => {
    checkAuth();
    // Re-check periodically or on focus if needed
    const interval = setInterval(checkAuth, 30000); 
    return () => clearInterval(interval);
  }, []);

  return (
    <AuthContext.Provider value={{ isAdmin, checkAuth }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
