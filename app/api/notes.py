from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api import deps
from app.models import models
from app.schemas import note, version
from app.crud import note_crud
from typing import List, Optional


router = APIRouter()

@router.post("/", response_model=note.Note)
def create_note(note_in: note.NoteCreate, db: Session = Depends(deps.get_db), current_user: models.User = Depends(deps.get_current_user)):
    new_note = models.Note(**note_in.model_dump(), owner_id=current_user.id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@router.put("/{note_id}", response_model=note.Note)
def update_note(note_id: int, note_in: note.NoteUpdate, db: Session = Depends(deps.get_db), current_user: models.User = Depends(deps.get_current_user)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == current_user.id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note_crud.update_note_with_versioning(db, note_id, note_in, current_user.id)

@router.get("/{note_id}/versions", response_model=List[version.NoteVersion])
def get_note_versions(note_id: int, db: Session = Depends(deps.get_db), current_user: models.User = Depends(deps.get_current_user)):
    versions = db.query(models.NoteVersion).filter(models.NoteVersion.note_id == note_id).all()
    return versions

@router.post("/{note_id}/restore/{version_num}", response_model=note.Note)
def restore_version(note_id: int, version_num: int, db: Session = Depends(deps.get_db), current_user: models.User = Depends(deps.get_current_user)):
   
    v = db.query(models.NoteVersion).filter(models.NoteVersion.note_id == note_id, models.NoteVersion.version_number == version_num).first()
    if not v:
        raise HTTPException(status_code=404, detail="Version not found")
    
   
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    db_note.content = v.content_snapshot
    db.commit()
    db.refresh(db_note)
    return db_note
  
  
@router.get("/", response_model=List[note.Note])
def read_notes(
    q: Optional[str] = None, # 'q' is the search query parameter
    db: Session = Depends(deps.get_db), 
    current_user: models.User = Depends(deps.get_current_user)
):
    
    query = db.query(models.Note).filter(models.Note.owner_id == current_user.id)
    
 
    if q:
    
        query = query.filter(
            models.Note.title.ilike(f"%{q}%") | 
            models.Note.content.ilike(f"%{q}%")
        )
    
    return query.all()

@router.get("/{note_id}", response_model=note.Note)
def read_note(note_id: int, db: Session = Depends(deps.get_db), current_user: models.User = Depends(deps.get_current_user)):
    n = db.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == current_user.id).first()
    if not n:
        raise HTTPException(status_code=404, detail="Note not found")
    return n

@router.delete("/{note_id}", status_code=204)
def delete_note(note_id: int, db: Session = Depends(deps.get_db), current_user: models.User = Depends(deps.get_current_user)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == current_user.id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(db_note)
    db.commit()
    return None
