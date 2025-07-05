import React, { useState } from 'react';

function App() {
  const [recommendations, setRecommendations] = useState([]);
  const [sentiment, setSentiment] = useState("");
  const [feedback, setFeedback] = useState("");
  const [userId] = useState("user123"); // Example static user

  const getRecommendations = async () => {
    const res = await fetch('/recommend', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ user_id: userId })
    });
    const data = await res.json();
    setRecommendations(data.recommendations);
  };

  const analyzeSentiment = async () => {
    const res = await fetch('/sentiment', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ feedback })
    });
    const data = await res.json();
    setSentiment(data.sentiment);
  };

  return (
    <div>
      <h1>Persona Shopper</h1>
      <button onClick={getRecommendations}>Get Recommendations</button>
      <ul>
        {recommendations.map((rec, i) => <li key={i}>{rec}</li>)}
      </ul>
      <h2>Feedback</h2>
      <input value={feedback} onChange={e => setFeedback(e.target.value)} />
      <button onClick={analyzeSentiment}>Analyze Sentiment</button>
      <p>Sentiment: {sentiment}</p>
      {/* Add AR/VR component here */}
    </div>
  );
}

export default App;
