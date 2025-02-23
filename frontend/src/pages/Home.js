// import React, { useState } from "react";
// import InputForm from "../components/InputForm";
// import ScoreDisplay from "../components/ScoreDisplay";
// import NewsList from "../components/NewsList";

// console.log("InputForm:", InputForm);
// console.log("ScoreDisplay:", ScoreDisplay);
// console.log("NewsList:", NewsList);
// console.log("Rendering Home.js");


// function Home() {
//   const [result, setResult] = useState(null);

//   return (
//     <div>
//       <h1>AI-Powered News Checker</h1>
//       <InputForm onResult={setResult} />
//       {result && <ScoreDisplay score={result.score} category={result.category} />}
//       <NewsList />
//     </div>
//   );
// }

// export default Home;

// import React, { useState } from "react";
// import InputForm from "../components/InputForm";
// import ScoreDisplay from "../components/ScoreDisplay";
// import NewsList from "../components/NewsList";

// function Home() {
//   const [result, setResult] = useState(null);

//   return (
//     <div className="container d-flex flex-column justify-content-center align-items-center text-center">
//       <h1>AI-Powered News Checker</h1>
//       <InputForm onResult={setResult} />
//       {result && <ScoreDisplay score={result.score} category={result.category} />}
//       <NewsList />
//     </div>
//   );
// }

// export default Home;



import React, { useState } from "react";
import InputForm from "../components/InputForm";
import ScoreDisplay from "../components/ScoreDisplay";
import NewsList from "../components/NewsList";

function Home() {
  const [result, setResult] = useState(null);

  return (
    <div 
      className="d-flex flex-column justify-content-center align-items-center text-center"
      style={{
        minHeight: "100vh",
        width: "100%",
        backgroundColor: "#f8f9fa",
        color: "#333",
        padding: "20px",
      }}
    >
      {/* Modern & Stylish Title */}
      <h1 
        style={{
          fontSize: "2.5rem",
          fontWeight: "bold",
          color: "#007bff",
          padding: "15px 30px",
          borderRadius: "10px",
          boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)",
          marginBottom: "30px",
          backgroundColor: "#ffffff",
        }}
      >
        AI-Powered News Checker
      </h1>

      <InputForm onResult={setResult} />
      
      {result && <ScoreDisplay score={result.score} category={result.category} />}
      
      <NewsList />
    </div>
  );
}

export default Home;
