#  Persona Shopper

> An AI-powered personal shopping assistant that combines a smart chatbot, voice interaction, and a full-stack web interface to deliver personalized product recommendations.

---

## Overview

**Persona Shopper** is a multi-modal AI shopping assistant that understands your preferences, answers product questions in natural language, and guides you to the right purchase — all through text or voice. It features a conversational chatbot backend powered by Python, a clean JavaScript frontend, and a dedicated voice interaction module for hands-free shopping.

---

## Features

- *AI Chatbot** — Conversational shopping assistant that understands user intent and recommends products
- **Voice Interface** — Hands-free interaction via a dedicated voice module
-  **Web Frontend** — Responsive JavaScript-based UI for seamless browsing and chat
-  **RESTful Backend** — Python-powered API layer handling business logic and AI responses
-  **Persona-based Recommendations** — Tailored suggestions based on user preferences and behavior

---

##  Project Structure

```
persona-shopper/
├── Voice/          # Voice input/output module for hands-free interaction
├── backend/        # Python API server — core logic, AI integration, data handling
├── chatbot/        # Chatbot engine — NLP, intent detection, response generation
└── frontend/       # JavaScript web interface — chat UI, product display
```

---

##  Tech Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Backend   | Python (Flask / FastAPI)          |
| Chatbot   | Python, NLP / LLM integration     |
| Frontend  | JavaScript (React / Vanilla JS)   |
| Voice     | Python speech libraries           |

> **Language split:** Python 59% · JavaScript 41%

---

##  Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+
- pip & npm

---

### 1. Clone the repository

```bash
git clone https://github.com/anandhivasudevan/persona-shopper.git
cd persona-shopper
```

---

### 2. Set up the Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

The backend server will start at `http://localhost:5000`.

---

### 3. Set up the Chatbot

```bash
cd chatbot
pip install -r requirements.txt
python chatbot.py
```

---

### 4. Set up the Frontend

```bash
cd frontend
npm install
npm start
```

The frontend will be available at `http://localhost:3000`.

---

### 5. (Optional) Enable Voice Interaction

```bash
cd Voice
pip install -r requirements.txt
python voice_main.py
```

---

##  Environment Variables

Create a `.env` file in the `backend/` directory:

```env
# Example environment variables
OPENAI_API_KEY=your_openai_api_key
PORT=5000
```

> Never commit your `.env` file. Add it to `.gitignore`.

---

##  Module Details

### `backend/`
The core API server. Handles HTTP requests from the frontend, orchestrates chatbot responses, and serves product data.

### `chatbot/`
The NLP/AI engine powering the conversational experience. Processes user messages, detects intent, and generates context-aware shopping recommendations.

### `frontend/`
The browser-based user interface. Provides a chat window, product browsing, and real-time responses from the AI backend.

### `Voice/`
A speech-enabled interface layer. Converts voice input to text and sends it to the chatbot engine, then reads the response aloud.

---

## Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is open source. See the [LICENSE](LICENSE) file for details.

---


---

> _Built with ❤️ to make shopping smarter, faster, and more personal._
