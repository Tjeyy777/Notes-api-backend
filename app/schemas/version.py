from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoteVersion(BaseModel):
    id: int
    note_id: int
    content_snapshot: str
    version_number: int
    created_at: datetime
    editor_id: Optional[int] = None  

    class Config:
        from_attributes = True