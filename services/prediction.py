import pandas as pd
from models.game import Game
from services.ml import model_columns, pre_process
from services.model import model

async def predict_game_rating(game: Game) -> float:
    game_dict = game.model_dump()
    renamed_dict = {
        'Game Title': game_dict['game_title'],
        'Year': game_dict['year'],
        'Publisher': game_dict['publisher'],
        'North America': game_dict['north_america'],
        'Europe': game_dict['europe'],
        'Japan': game_dict['japan'],
        'Rest of World': game_dict['rest_of_world'],
        'Global': game_dict['global_sales'],
        'Number of Reviews': game_dict['number_of_reviews'],
        'Wishlist': game_dict['wishlist'],
        'Platform': game_dict['platform'],
        'Genre': game_dict['genre']
    }
    
    # Create DataFrame with correct column names
    features = pd.DataFrame([renamed_dict])
    
    features = pre_process(features)
    features = features.reindex(columns=model_columns, fill_value=0)
    
    rating = model.predict(features)[0]
    
    return rating