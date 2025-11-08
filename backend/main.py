# backend/main.py

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session
from typing import List

# Diğer Python dosyalarımızı 'from .' OLMADAN, doğrudan import ediyoruz
import crud
import models
import schemas
import database

# Uygulama başlarken veritabanını ve tabloları oluştur
database.create_db_and_tables()

app = FastAPI(title="BİT Envanter API", version="1.0")

# --- CORS Ayarı ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # React uygulamasının adresi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- API ENDPOINTLERİ (Rotalar) ---

@app.get("/")
def read_root():
    return {"message": "BİT Envanter API'sine hoş geldiniz. /docs adresini ziyaret edin."}

# --- Ekipman Rotaları ---

@app.post("/api/equipment", response_model=schemas.EquipmentRead)
def create_new_equipment(
    equipment: schemas.EquipmentCreate, 
    session: Session = Depends(database.get_session)
):
    return crud.create_equipment(session=session, equipment=equipment)

@app.get("/api/equipment", response_model=List[schemas.EquipmentRead])
def read_all_equipment(session: Session = Depends(database.get_session)):
    return crud.get_equipment_list(session=session)

# --- Arıza Kaydı (Ticket) Rotaları ---

@app.post("/api/tickets", response_model=schemas.TicketRead)
def create_new_ticket(
    ticket: schemas.TicketCreate, 
    session: Session = Depends(database.get_session)
):
    db_ticket = crud.create_ticket(session=session, ticket=ticket)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ekipman bulunamadı")
    return db_ticket

@app.get("/api/tickets", response_model=List[schemas.TicketReadWithEquipment])
def read_all_tickets(
    durum: str | None = None, 
    session: Session = Depends(database.get_session)
):
    tickets = crud.get_tickets(session=session, durum=durum)
    result = []
    
    for ticket in tickets:
        db_equipment = crud.get_equipment_by_id(session, ticket.cihaz_id)
        
        ticket_with_equipment = schemas.TicketReadWithEquipment(
            id=ticket.id,
            bildiren=ticket.bildiren,
            aciklama=ticket.aciklama,
            durum=ticket.durum,
            cihaz_id=ticket.cihaz_id,
            cihaz=db_equipment
        )
        result.append(ticket_with_equipment)
        
    return result

@app.put("/api/tickets/{ticket_id}/resolve", response_model=schemas.TicketRead)
def resolve_existing_ticket(
    ticket_id: int, 
    session: Session = Depends(database.get_session)
):
    db_ticket = crud.resolve_ticket(session=session, ticket_id=ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Arıza kaydı bulunamadı")
    return db_ticket