from ninja import Schema

class MovieOut(Schema):
    id: int
    name: str
    email: str
    image: str


class UserOut(Schema):
    id: int
    name: str
    category: str
    image: str
