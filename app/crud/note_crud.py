from sqlalchemy.orm import Session
from app.models import models
from app.schemas import note as note_schema

def update_note_with_versioning(db: Session, note_id: int, note_in: note_schema.NoteUpdate, user_id: int):
   
    db_note = db.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == user_id).first()
    
    if not db_note:
        return None

   
    version_history = models.NoteVersion(
        note_id=db_note.id,
        content_snapshot=db_note.content,
        version_number=len(db_note.versions) + 1
    )
    db.add(version_history)


    db_note.title = note_in.title
    db_note.content = note_in.content
    
    db.commit()
    db.refresh(db_note)
    return db_note