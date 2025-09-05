import React from 'react';
import AgentChat from './AgentChat';

function App() {
  return (
    <div style={{ maxWidth: 600, margin: '50px auto', padding: '30px', border: '1px solid #ddd', borderRadius: 8 }}>
      <h2>Agentic AI Assistant Chat</h2>
      <AgentChat />
    </div>
  );
}

export default App;