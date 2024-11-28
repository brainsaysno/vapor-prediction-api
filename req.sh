curl "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{
    "id": 2,
    "Game Title": "My Little Pony: Pinkie Pies Party",
    "Year": 2008,
    "Publisher": "THQ",
    "North America": 0.72,
    "Europe": 0.00,
    "Japan": 0.0,
    "Rest of World": 0.06,
    "Global": 0.78,
    "Number of Reviews": 100,
    "Wishlist": 100,
    "Platform": "DS",
    "Genre": "Adventure"
}'
