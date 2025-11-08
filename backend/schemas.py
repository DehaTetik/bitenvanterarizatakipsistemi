from sqlmodel import SQLModel

# --- Equipment Şemaları ---
class EquipmentBase(SQLModel):
    cihaz_turu: str
    marka_model: str
    zimmetli_personel: str

class EquipmentCreate(EquipmentBase):
    pass # Ekstra alan yok

class EquipmentRead(EquipmentBase):
    id: int
    durum: str

# --- Ticket Şemaları ---
class TicketBase(SQLModel):
    bildiren: str
    aciklama: str
    cihaz_id: int

class TicketCreate(TicketBase):
    pass # Ekstra alan yok

class TicketRead(TicketBase):
    id: int
    durum: str

# --- Bileşik Şema (Çok Önemli) ---
# Arıza kaydını ve ilgili cihaz bilgisini BİRLİKTE göstermek için
class TicketReadWithEquipment(TicketRead):
    cihaz: EquipmentRead # İç içe model