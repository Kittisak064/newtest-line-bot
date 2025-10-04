# LINE Chatbot (FastAPI + Render)

## Run local
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Deploy on Render
- Push to GitHub
- Connect repo to Render Web Service
- Add ENV vars:
  - OPENAI_API_KEY
  - LINE_CHANNEL_SECRET
  - LINE_CHANNEL_ACCESS_TOKEN
- Set Webhook URL in LINE Developers: 
  `https://<your-app>.onrender.com/webhook/line`
