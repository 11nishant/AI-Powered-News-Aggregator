// import React, { useState, useEffect } from "react";
// import axios from "../services/api";

// function AdminPanel() {
//   const [news, setNews] = useState([]);

//   useEffect(() => {
//     axios.get("/news").then((res) => setNews(res.data));
//   }, []);

//   const deleteNews = async (id) => {
//     await axios.delete(`/news/${id}`);
//     setNews(news.filter((item) => item.id !== id));
//   };

//   return (
//     <div>
//       <h1>Admin Panel</h1>
//       <ul>
//         {news.map((item) => (
//           <li key={item.id} className="list-group-item d-flex justify-content-between"  >
//             {item.headline} - {item.score}%
//             <button className="btn btn-danger btn-sm" onClick={() => deleteNews(item.id)}>Delete</button>
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// }

// export default AdminPanel;



import React, { useState, useEffect } from "react";
import axios from "../services/api";

function AdminPanel() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    axios
      .get("/news")
      .then((res) => setNews(res.data))
      .catch((err) => console.error("Error fetching news:", err));
  }, []);

  const deleteNews = async (id) => {
    try {
      await axios.delete(`/news/${id}`);
      setNews(news.filter((item) => item.id !== id));
    } catch (error) {
      console.error("Error deleting news:", error);
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4 fw-bold text-primary">Admin Panel</h1>

      <div className="card shadow-lg p-4 rounded-3">
        <ul className="list-group">
          {news.map((item) => (
            <li
              key={item.id}
              className="list-group-item d-flex justify-content-between align-items-center p-3"
              style={{ borderRadius: "10px", background: "#f8f9fa" }}
            >
              <div>
                <h5 className="mb-1 fw-semibold text-dark">{item.headline}</h5>
                <small className="text-muted">Conspiracy Score: {item.score}%</small>
              </div>
              <button
                className="btn btn-danger btn-sm px-3 shadow-sm"
                onClick={() => deleteNews(item.id)}
              >
                Delete
              </button>
            </li>
          ))}
        </ul>

        {news.length === 0 && (
          <p className="text-center text-muted mt-3">No news available.</p>
        )}
      </div>
    </div>
  );
}

export default AdminPanel;
