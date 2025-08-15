from pydandic import BaseModel
from datetime import datetime
from typing import Optional

class NewsOut(BaseModel):
    id:int
    title:str
    link:str
    type:int
    push_date:Optional[datetime]
    content:str
    source:str

    class Config:
        from_attributes = True


