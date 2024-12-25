import React, { useEffect, useState } from "react";
import api from "../api/api";
import { useSelector } from "react-redux";

const AdminPage = () => {
  const { token } = useSelector((state) => state.auth);
  const [users, setUsers] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const res = await api.get("/admin/users/", {
        headers: { Authorization: `Bearer ${token}` },
      });
      setUsers(res.data);
    } catch (err) {
      setError("Ошибка при получении списка пользователей.");
    }
  };

  const handleDeleteUser = async (userId) => {
    try {
      await api.delete(`/admin/users/${userId}/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      fetchUsers();
    } catch (err) {
      setError("Ошибка при удалении пользователя.");
    }
  };

  return (
    <div>
      <h1>Админ-панель</h1>
      {error && <p style={{ color: "red" }}>{error}</p>}

      <h2>Список пользователей:</h2>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.username} ({user.email})
            <button onClick={() => handleDeleteUser(user.id)}>Удалить</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AdminPage;
