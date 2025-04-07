from pydantic import BaseModel
from typing import List, Optional

class TopicClass(BaseModel):
    topic: str
