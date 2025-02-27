# AI Chatbot with Node.js + EJS Frontend and Python + LangChain Backend

This project implements a modern chatbot using Node.js with EJS for the frontend and Python with LangChain for the backend.

## Prerequisites

- Node.js (v14 or higher)
- Python (v3.8 or higher)
- Google API Key for Gemini

## Project Structure

```
chatbot/
├── frontend/
│   ├── app.js
│   ├── views/
│   │   └── index.ejs
│   ├── public/
│   └── package.json
├── backend/
│   ├── app.py
│   └── requirements.txt
└── .env
```

## Setup Instructions

1. Frontend Setup:

```bash
cd frontend
npm init -y
npm install express ejs axios dotenv
```

2. Backend Setup:

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install flask flask-cors langchain langchain-google-genai python-dotenv
```

3. Create .env file in the root directory:

```
GOOGLE_API_KEY=your_google_api_key
PORT=3000
```

4. Start the servers:

- Frontend: `node app.js`
- Backend: `python app.py`

## Usage

1. Open your browser and navigate to `http://localhost:3000`
2. Start chatting with the AI bot
3. The chat interface will display both user messages and AI responses

## Features

- Modern, responsive UI using Tailwind CSS
- Real-time chat interface
- Conversation memory using LangChain
- Integration with Gemini AI model
- Error handling and loading states

## Development

- Frontend code is in `frontend/app.js` and `frontend/views/index.ejs`
- Backend code is in `backend/app.py`
- Modify the UI in `index.ejs`
- Adjust AI parameters in `app.py`

## Deployment

1. Choose a hosting platform (e.g., Heroku, DigitalOcean)
2. Set up environment variables on your hosting platform
3. Deploy frontend and backend separately
4. Update API endpoints in frontend code to match your deployed backend URL

## Security Considerations

- Never commit your .env file
- Implement rate limiting
- Add input validation
- Consider adding user authentication
- Secure your API endpoints

## Contributing

Feel free to submit issues and enhancement requests!
