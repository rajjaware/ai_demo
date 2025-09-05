import React, { useState, useContext } from 'react';
import axios from 'axios';
import { AuthContext } from './AuthContext';

export default function ChatAssistant() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const { token } = useContext(AuthContext);

  const sendMessage = async () => {
    setMessages([...messages, { from: 'user', text: input }]);
    const res = await axios.post('http://localhost:8000/api/chat-assistant/', { message: input }, {
      headers: { Authorization: `Bearer ${token}` }
    });
    setMessages([...messages, { from: 'user', text: input }, { from: 'ai', text: res.data.response }]);
    setInput('');
  };

  return (
    <div>
      <div>
        {messages.map((msg, i) => (
          <div key={i} style={{ textAlign: msg.from === 'ai' ? 'left' : 'right' }}>
            <b>{msg.from}:</b> {msg.text}
          </div>
        ))}
      </div>
      <input value={input} onChange={e=>setInput(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}