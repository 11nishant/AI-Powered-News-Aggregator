import React, { useEffect, useState } from "react";
import axios from "../services/api";

function NewsList() {
    console.log("Rendering NewsList.js");
  const [news, setNews] = useState([]);

  useEffect(() => {
    axios.get("/news").then((res) => setNews(res.data));
  }, []);

  return (
    <ul>
      {news.map((item, index) => (
        <li key={index}>{item.headline} - {item.score}%</li>
      ))}
    </ul>
  );
}

export default NewsList;
