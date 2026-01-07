from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List, Optional

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    # Updated: Use model_config instead of class Config
    model_config = ConfigDict(from_attributes=True)


class NoteVersion(BaseModel):
    id: int
    note_id: int
    content_snapshot: str
    version_number: int
    created_at: datetime
    
    editor_id: Optional[int] = None 

    # Updated: Use model_config instead of class Config
    model_config = ConfigDict(from_attributes=True)