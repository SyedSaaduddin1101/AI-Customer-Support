from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_ticket, get_tickets, get_ticket, update_ticket, delete_ticket
from schemas import TicketCreate, TicketUpdate, TicketResponse
from typing import List

router = APIRouter(prefix="/tickets", tags=["Tickets"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TicketResponse)
def create(ticket: TicketCreate, db: Session = Depends(get_db)):
    return create_ticket(db, ticket)

@router.get("/", response_model=List[TicketResponse])
def read_all(db: Session = Depends(get_db)):
    return get_tickets(db)

@router.get("/{ticket_id}", response_model=TicketResponse)
def read_one(ticket_id: int, db: Session = Depends(get_db)):
    ticket = get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@router.patch("/{ticket_id}", response_model=TicketResponse)
def update(ticket_id: int, ticket: TicketUpdate, db: Session = Depends(get_db)):
    updated_ticket = update_ticket(db, ticket_id, ticket)
    if not updated_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return updated_ticket

@router.delete("/{ticket_id}")
def delete(ticket_id: int, db: Session = Depends(get_db)):
    deleted_ticket = delete_ticket(db, ticket_id)
    if not deleted_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"detail": "Ticket deleted"}
