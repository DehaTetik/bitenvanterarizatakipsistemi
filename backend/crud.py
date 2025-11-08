from sqlmodel import Session, select
import models 
import schemas

# --- CRUD for Equipment ---

def create_equipment(session: Session, equipment: schemas.EquipmentCreate) -> models.Equipment:
    # Şemayı (schemas.EquipmentCreate) modele (models.Equipment) dönüştür
    db_equipment = models.Equipment.model_validate(equipment)
    session.add(db_equipment)
    session.commit()
    session.refresh(db_equipment)
    return db_equipment

def get_equipment_list(session: Session) -> list[models.Equipment]:
    equipments = session.exec(select(models.Equipment)).all()
    return equipments

def get_equipment_by_id(session: Session, equipment_id: int) -> models.Equipment | None:
    return session.get(models.Equipment, equipment_id)

# --- CRUD for Tickets ---

def create_ticket(session: Session, ticket: schemas.TicketCreate) -> models.Ticket:
    # 1. Cihazı bul ve durumunu "Arızalı" yap
    db_equipment = get_equipment_by_id(session, ticket.cihaz_id)
    if not db_equipment:
        return None # Hata yönetimi için (main.py'de 404'e çevrilecek)
    
    db_equipment.durum = "Arızalı"
    
    # 2. Yeni arıza kaydını oluştur
    db_ticket = models.Ticket.model_validate(ticket)
    
    session.add(db_equipment)
    session.add(db_ticket)
    session.commit()
    session.refresh(db_ticket)
    return db_ticket

def get_tickets(session: Session, durum: str | None = None) -> list[models.Ticket]:
    statement = select(models.Ticket)
    if durum:
        statement = statement.where(models.Ticket.durum == durum)
    
    tickets = session.exec(statement).all()
    return tickets

def resolve_ticket(session: Session, ticket_id: int) -> models.Ticket | None:
    # 1. Arıza kaydını bul
    db_ticket = session.get(models.Ticket, ticket_id)
    if not db_ticket:
        return None # Kayıt bulunamadı
    
    # 2. Cihazı bul
    db_equipment = get_equipment_by_id(session, db_ticket.cihaz_id)
    
    # 3. Durumları güncelle
    db_ticket.durum = "Çözüldü"
    if db_equipment:
        db_equipment.durum = "Aktif"
        session.add(db_equipment)
        
    session.add(db_ticket)
    session.commit()
    session.refresh(db_ticket)
    return db_ticket