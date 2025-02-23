

// import React, { useState } from "react";
// import axios from "../services/api";

// function InputForm({ onResult }) {
//   const [headline, setHeadline] = useState("");
//   const [loading, setLoading] = useState(false);

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     setLoading(true);

//     try {
//       const response = await axios.post("/predict", { headline });

//       // Extract required fields
//       const { conspiracy_score, sentiment } = response.data;

//       // Mapping sentiment to a user-friendly category
//       const categoryMap = {
//         NEGATIVE: "Misinformation",
//         POSITIVE: "Reliable",
//         NEUTRAL: "Uncertain",
//       };

//       // Update state with formatted response
//       onResult({
//         score: conspiracy_score, // Pass conspiracy_score
//         category: categoryMap[sentiment] || "Unknown", // Convert sentiment to category
//       });
//     } catch (error) {
//       console.error("Error fetching score:", error);
//       onResult({ score: "Error", category: "Could not fetch data" });
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="container mt-3">
//       <form onSubmit={handleSubmit} className="d-flex">
//         <input
//           type="text"
//           className="form-control me-2"
//           value={headline}
//           onChange={(e) => setHeadline(e.target.value)}
//           placeholder="Enter a news headline"
//           required
//         />
//         <button type="submit" className="btn btn-primary">
//           {loading ? "Checking..." : "Check"}
//         </button>
//       </form>
//     </div>
//   );
// }

// export default InputForm;


import React, { useState } from "react";
import axios from "../services/api";

function InputForm({ onResult }) {
  const [headline, setHeadline] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await axios.post("/predict", { headline });

      // Extract required fields
      const { conspiracy_score, sentiment } = response.data;

      // Mapping sentiment to a user-friendly category
      const categoryMap = {
        NEGATIVE: "Misinformation",
        POSITIVE: "Reliable",
        NEUTRAL: "Uncertain",
      };

      // Update state with formatted response
      onResult({
        score: conspiracy_score,
        category: categoryMap[sentiment] || "Unknown",
      });
    } catch (error) {
      console.error("Error fetching score:", error);
      onResult({ score: "Error", category: "Could not fetch data" });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={containerStyle}>
      <form onSubmit={handleSubmit} style={formStyle}>
        <input
          type="text"
          style={inputStyle}
          value={headline}
          onChange={(e) => setHeadline(e.target.value)}
          placeholder="Enter a news headline..."
          required
        />
        <button type="submit" style={buttonStyle}>
          {loading ? "Checking..." : "Check"}
        </button>
      </form>
    </div>
  );
}

// Modern, Clean Styles with Proper Spacing
const containerStyle = {
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  marginTop: "80px", // Increased margin to push it down below the navbar
};

const formStyle = {
  display: "flex",
  gap: "10px",
  width: "100%",
  maxWidth: "500px",
};

const inputStyle = {
  flex: 1,
  padding: "12px",
  fontSize: "16px",
  border: "1px solid #ccc",
  borderRadius: "8px",
  outline: "none",
};

const buttonStyle = {
  padding: "12px 18px",
  fontSize: "16px",
  backgroundColor: "#007bff",
  color: "white",
  border: "none",
  borderRadius: "8px",
  cursor: "pointer",
  transition: "background 0.3s ease",
};

export default InputForm;
