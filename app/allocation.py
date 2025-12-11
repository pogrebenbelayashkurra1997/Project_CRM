import random
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Operator, Contact

def count_active_for_operator(db: Session, operator_id: int) -> int:
    return (
        db.query(func.count(Contact.id))
        .filter(Contact.operator_id == operator_id, Contact.status == "active")
        .scalar() or 0
    )

def allocate_operator_for_source(db: Session, source: Operator | None):
    rows = db.query(Operator.id, Operator.weight).filter(Operator.source_id == source.id).all()

    candidates = []
    weights = []

    for op_id, w in rows:
        op = db.get(Operator, op_id)
        if not op or not op.active:
            continue
        if count_active_for_operator(db, op.id) >= op.limit:
            continue
        candidates.append(op)
        weights.append(max(1, w))

    if not candidates:
        return None

    while candidates:
        chosen = random.choices(candidates, weights=weights, k=1)[0]
        if count_active_for_operator(db, chosen.id) < chosen.limit:
            return chosen
        idx = candidates.index(chosen)
        candidates.pop(idx)
        weights.pop(idx)

    return None
