// import React from "react";

// function ScoreDisplay({ score, category }) {
//   return (
//     <div className="alert alert-info mt-3">
//       <h3>Conspiracy Score: {score}%</h3>
//       <p>Category: {category}</p>
//     </div>
//   );
// }

// export default ScoreDisplay;


import React from "react";

function ScoreDisplay({ score, category }) {
  return (
    <div className="alert alert-info mt-3">
      <h3>Conspiracy Score: {score ? `${score}%` : "N/A"}</h3>
      <p>Category: {category || "Unknown"}</p>
    </div>
  );
}

export default ScoreDisplay;
