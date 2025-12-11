from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Lead

router = APIRouter(prefix="/leads", tags=["leads"])

@router.get("/")
def list_leads(db: Session = Depends(get_db)):
    leads = db.query(Lead).all()
    out = []
    for l in leads:
        out.append({
            "id": l.id,
            "external_id": l.external_id,
            "phone": l.phone,
            "contacts": [
                {"id": c.id, "source": c.source.name, "operator_id": c.operator_id, "status": c.status}
                for c in l.contacts
            ]
        })
    return out
