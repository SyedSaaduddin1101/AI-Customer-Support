from sqlalchemy.orm import Session
from models import Ticket
from schemas import TicketCreate, TicketUpdate

def create_ticket(db: Session, ticket: TicketCreate):
    db_ticket = Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_tickets(db: Session, skip: int =0, limit:int=100):
    return db.query(Ticket).offset(skip).limit(limit).all()

def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def update_ticket(db: Session, ticket_id: int, updates: TicketUpdate):
    db_ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    if not ticket:
        return None

    if updates.title is not None:
        ticket.title = updates.title
    if updates.description is not None:
        ticket.description = updates.description
    if updates.status is not None:
        ticket.status = updates.status

    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def delete_ticket(db: Session, ticket_id: int):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not db_ticket:
        return None
    db.delete(db_ticket)
    db.commit()
    return db_ticket
