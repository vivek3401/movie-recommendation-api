from pydantic import BaseModel

class MovieRequest(BaseModel):
    movie: str