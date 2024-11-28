from pydantic import BaseModel, Field

class Game(BaseModel):
    id: int
    game_title: str = Field(alias='Game Title')
    year: int = Field(alias='Year')
    publisher: str = Field(alias='Publisher')
    north_america: float = Field(alias='North America')
    europe: float = Field(alias='Europe')
    japan: float = Field(alias='Japan')
    rest_of_world: float = Field(alias='Rest of World')
    global_sales: float = Field(alias='Global')
    number_of_reviews: int = Field(alias='Number of Reviews')
    wishlist: int = Field(alias='Wishlist')
    platform: str = Field(alias='Platform')
    genre: str = Field(alias='Genre')

    class Config:
        populate_by_name = True