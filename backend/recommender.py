import random

def get_recommendations(user_id, db):
    # Fetch user profile and history
    user = db.users.find_one({"user_id": user_id}) or {}
    interests = user.get("interests", ["fashion", "tech", "beauty"])
    # Dummy recommender logic (replace with ML model)
    products = db.products.find({"category": {"$in": interests}})
    recommendations = [p["name"] for p in products]
    if not recommendations:
        recommendations = ["Default Product A", "Default Product B"]
    return random.sample(recommendations, min(3, len(recommendations)))
