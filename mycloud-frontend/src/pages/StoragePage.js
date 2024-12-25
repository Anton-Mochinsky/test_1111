import React, { useEffect, useState } from "react";
import api from "../api/api";
import { useSelector } from "react-redux";

const StoragePage = () => {
  const { token } = useSelector((state) => state.auth);
  const [files, setFiles] = useState([]);
  const [file, setFile] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchFiles();
  }, []);

  const fetchFiles = async () => {
    try {
      const res = await api.get("/files/", {
        headers: { Authorization: `Bearer ${token}` },
      });
      setFiles(res.data);
    } catch (err) {
      setError("Ошибка при получении файлов.");
    }
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", file);

    try {
      await api.post("/files/upload/", formData, {
        headers: { 
          Authorization: `Bearer ${token}`,
          "Content-Type": "multipart/form-data",
        },
      });
      fetchFiles();
      setFile(null);
    } catch (err) {
      setError("Ошибка при загрузке файла.");
    }
  };

  const handleDelete = async (fileId) => {
    try {
      await api.delete(`/files/${fileId}/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      fetchFiles();
    } catch (err) {
      setError("Ошибка при удалении файла.");
    }
  };

  return (
    <div>
      <h1>Мое хранилище</h1>
      {error && <p style={{ color: "red" }}>{error}</p>}
      
      <form onSubmit={handleUpload}>
        <input 
          type="file" 
          onChange={(e) => setFile(e.target.files[0])} 
          required 
        />
        <button type="submit">Загрузить файл</button>
      </form>

      <h2>Список файлов:</h2>
      <ul>
        {files.map((file) => (
          <li key={file.id}>
            <a href={file.url} target="_blank" rel="noopener noreferrer">
              {file.name}
            </a>
            <button onClick={() => handleDelete(file.id)}>Удалить</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default StoragePage;
