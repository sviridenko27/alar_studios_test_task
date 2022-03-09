from sqlmodel import SQLModel


# TODO: rename to real name not abstract
class Item(SQLModel):
    """
    Form for data from remote services.
    """
    id: int
    name: str
