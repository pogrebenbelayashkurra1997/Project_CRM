from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Lead, Source, Contact
from app.schemas import ContactCreate, ContactRead
from app.allocation import allocate_operator_for_source

router = APIRouter(prefix="/contacts", tags=["contacts"])

@router.post("/", response_model=ContactRead)
def create_contact(data: ContactCreate, db: Session = Depends(get_db)):
    lead = None
    if data.lead.external_id:
        lead = db.query(Lead).filter(Lead.external_id == data.lead.external_id).first()
    if not lead and data.lead.phone:
        lead = db.query(Lead).filter(Lead.phone == data.lead.phone).first()
    if not lead:
        lead = Lead(external_id=data.lead.external_id, phone=data.lead.phone)
        db.add(lead)
        db.commit()
        db.refresh(lead)

    source = db.query(Source).filter(Source.name == data.source_name).first()
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")

    operator = allocate_operator_for_source(db, source)

    contact = Contact(
        lead_id=lead.id,
        source_id=source.id,
        operator_id=operator.id if operator else None,
        payload=data.payload
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact
