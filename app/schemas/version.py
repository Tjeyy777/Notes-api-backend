from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class NoteVersion(BaseModel):
    id: int
    note_id: int
    content_snapshot: str
    version_number: int
    created_at: datetime
    editor_id: Optional[int] = None

    
    model_config = ConfigDict(from_attributes=True)