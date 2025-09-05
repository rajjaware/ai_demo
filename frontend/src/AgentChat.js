import React, { useState } from 'react';
import axios from 'axios';

export default function AgentChat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    setMessages([...messages, { from: 'user', text: input }]);
    const res = await axios.post('http://localhost:5000/chat', { message: input });
    setMessages([...messages, { from: 'user', text: input }, { from: 'agent', text: res.data.response }]);
    setInput('');
  };

  return (
    <div>
      <div>
        {messages.map((msg, i) => (
          <div key={i} style={{ textAlign: msg.from === 'agent' ? 'left' : 'right' }}>
            <b>{msg.from}:</b> {msg.text}
          </div>
        ))}
      </div>
      <input value={input} onChange={e=>setInput(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}