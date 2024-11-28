from fastapi import FastAPI, HTTPException
from models.game import Game
from services.prediction import predict_game_rating

app = FastAPI()

@app.post("/predict")
async def predict(game: Game):
    try:
        rating = await predict_game_rating(game)
        return {
            "game_title": game.game_title,
            "predicted_rating": float(rating)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
