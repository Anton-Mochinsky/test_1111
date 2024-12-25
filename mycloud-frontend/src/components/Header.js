import React from "react";
import { Link } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { logout } from "../redux/slices/authSlice";

const Header = () => {
  const { isAuthenticated, user } = useSelector((state) => state.auth);
  const dispatch = useDispatch();

  const handleLogout = () => {
    dispatch(logout());
  };

  return (
    <nav>
      <ul>
        <li><Link to="/">Главная</Link></li>
        {!isAuthenticated ? (
          <>
            <li><Link to="/login">Вход</Link></li>
            <li><Link to="/register">Регистрация</Link></li>
          </>
        ) : (
          <>
            {user?.isAdmin && <li><Link to="/admin">Админ-панель</Link></li>}
            <li><Link to="/storage">Мое хранилище</Link></li>
            <li>
              <button onClick={handleLogout}>Выход</button>
            </li>
          </>
        )}
      </ul>
    </nav>
  );
};

export default Header;
