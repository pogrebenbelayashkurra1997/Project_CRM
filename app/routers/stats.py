from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db import get_db
from app.models import Contact

router = APIRouter(prefix="/stats", tags=["stats"])

@router.get("/distribution/")
def distribution_stats(db: Session = Depends(get_db)):
    q = db.query(Contact.source_id, Contact.operator_id, func.count(Contact.id)).group_by(Contact.source_id, Contact.operator_id).all()
    return [{"source_id": s, "operator_id": o, "count": cnt} for s, o, cnt in q]
