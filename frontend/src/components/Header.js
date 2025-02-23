// import React from "react";
// import { Link } from "react-router-dom";

// function Header() {
//   return (
//     <nav className="navbar navbar-light bg-light container d-flex justify-content-center">
//       <ul>
//         <li><Link to="/">Home</Link></li>
//         <li><Link to="/admin">Admin Panel</Link></li>
//       </ul>
//     </nav>
//   );
// }

// export default Header;

import React from "react";
import { Link } from "react-router-dom";

function Header() {
  return (
    <nav style={navbarStyle}>
      <div style={containerStyle}>
        <h2 style={logoStyle}>News Dashboard</h2>
        <ul style={navListStyle}>
          <li><Link style={linkStyle} to="/">Home</Link></li>
          <li><Link style={linkStyle} to="/admin">Admin Panel</Link></li>
        </ul>
      </div>
    </nav>
  );
}

// Modern Minimalist Styles
const navbarStyle = {
  background: "#fff",
  padding: "12px 20px",
  boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)",
  borderBottom: "2px solid #007bff",
};

const containerStyle = {
  display: "flex",
  justifyContent: "space-between",
  alignItems: "center",
  maxWidth: "1100px",
  margin: "0 auto",
};

const logoStyle = {
  color: "#333",
  fontSize: "1.6rem",
  fontWeight: "bold",
};

const navListStyle = {
  display: "flex",
  listStyle: "none",
  gap: "20px",
  padding: 0,
};

const linkStyle = {
  textDecoration: "none",
  color: "#007bff",
  fontSize: "1.1rem",
  fontWeight: "500",
  transition: "color 0.3s ease",
};

export default Header;

