from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, crud, schemas
from fastapi.middleware.cors import CORSMiddleware
# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SupportIQ Backend")
# Allow your frontend to talk to backend
origins = [
    "http://localhost:5500",  # If you open index.html with Live Server or similar
    "http://127.0.0.1:5500",
    "http://localhost:8000",
    "http://127.0.0.1:8000", # optional if calling from backend itself
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # front-end URL(s)
    allow_credentials=True,
    allow_methods=["*"],        # GET, POST, PATCH, DELETE, etc.
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Ticket
@app.post("/tickets/", response_model=schemas.TicketResponse)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    return crud.create_ticket(db, ticket)

# Get All Tickets
@app.get("/tickets/", response_model=list[schemas.TicketResponse])
def read_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tickets(db, skip, limit)

# Get Single Ticket
@app.get("/tickets/{ticket_id}", response_model=schemas.TicketResponse)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = crud.get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

# Update Ticket
@app.put("/tickets/{ticket_id}", response_model=schemas.TicketResponse)
def update_ticket(ticket_id: int, updates: schemas.TicketUpdate, db: Session = Depends(get_db)):
    ticket = crud.update_ticket(db, ticket_id, updates)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

# Delete Ticket
@app.delete("/tickets/{ticket_id}", response_model=schemas.TicketResponse)
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = crud.delete_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket
# Partial update (PATCH)
@app.patch("/tickets/{ticket_id}", response_model=schemas.TicketResponse)
def patch_ticket(ticket_id: int, updates: schemas.TicketUpdate, db: Session = Depends(get_db)):
    ticket = crud.update_ticket(db, ticket_id, updates)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket
