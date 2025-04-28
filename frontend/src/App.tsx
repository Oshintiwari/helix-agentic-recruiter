import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

type MessageType = "user" | "ai";

type Message = {
  type: MessageType;
  text: string;
};

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [sequence, setSequence] = useState<string[]>([]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const newMessages: Message[] = [...messages, { type: "user", text: input }];
    setMessages(newMessages);
    setInput('');

    try {
      const response = await axios.post('http://127.0.0.1:5000/chat', { message: input });


      const aiText = response.data.response || "No AI response.";

      const updatedMessages: Message[] = [...newMessages, { type: "ai", text: aiText }];
      setMessages(updatedMessages);

      const splitSteps = aiText.split(/\b(Step\s*\d+:|Email\s*\d+:|Subject:)/i)
        .map((step: string) => step.trim())
        .filter((step: string) => step.length > 0);

      setSequence(splitSteps);

    } catch (error) {
      console.error('Error contacting AI server:', error);
      setMessages([...newMessages, { type: "ai", text: "Error contacting AI server." }]);
    }
  };

  return (
    <div className="app-container">
      <div className="header">
        <div className="column-header">Chat</div>
        <div className="column-header">Workspace</div>
      </div>

      <div className="main-content">
        <div className="chat-section">
          <div className="chat-box">
            {messages.map((msg, idx) => (
              <div key={idx} className={msg.type === 'user' ? 'user-bubble' : 'ai-bubble'}>
                {msg.text}
              </div>
            ))}
          </div>
          <div className="input-box">
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type your message..."
            />
            <button onClick={handleSend}>Send</button>
          </div>
        </div>

        <div className="workspace-section">
          <div className="workspace-box">
            {sequence.length === 0 ? (
              <div className="no-sequence">No sequence generated.</div>
            ) : (
              sequence.map((step, idx) => (
                <div key={idx} className="step-card">
                  {step}
                </div>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
