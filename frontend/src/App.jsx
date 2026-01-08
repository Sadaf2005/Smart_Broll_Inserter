import { useState } from "react";

function App() {
  const [timeline, setTimeline] = useState(null);
  const [loading, setLoading] = useState(false);

  const generatePlan = async () => {
    setLoading(true);
    const res = await fetch("http://localhost:8000/generate-plan", {
      method: "POST",
    });
    const data = await res.json();
    setTimeline(data);
    setLoading(false);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h2>Smart B-Roll Inserter</h2>

      <button onClick={generatePlan} disabled={loading}>
        {loading ? "Generating..." : "Generate Timeline Plan"}
      </button>

      {timeline && (
        <pre
    style={{
      marginTop: "2rem",
      backgroundColor: "#f4f4f4",
      color: "#000000",
      padding: "1rem",
      borderRadius: "6px",
      maxHeight: "400px",
      overflow: "auto",
      fontSize: "14px",
    }}
  >
          {JSON.stringify(timeline, null, 2)}
        </pre>
      )}
    </div>
  );
}

export default App;
