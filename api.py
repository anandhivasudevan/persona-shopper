from fastapi import FastAPI, Request
from backend.recommender import get_recommendations
from backend.sentiment import analyze_sentiment
from pymongo import MongoClient

app = FastAPI()

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["persona_shopper"]

@app.post("/recommend")
async def recommend(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    recommendations = get_recommendations(user_id, db)
    return {"recommendations": recommendations}

@app.post("/sentiment")
async def sentiment(request: Request):
    data = await request.json()
    feedback = data.get("feedback")
    sentiment = analyze_sentiment(feedback)
    return {"sentiment": sentiment}

@app.get("/dynamic-content/{user_id}")
async def dynamic_content(user_id: str):
    # Example: fetch user profile and personalize content
    user = db.users.find_one({"user_id": user_id})
    content = {
        "greeting": f"Hello, {user.get('name', 'shopper')}!",
        "personalized_banner": f"Deals for {user.get('favorite_category', 'you')}"
    }
    return content