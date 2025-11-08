from sqlmodel import Field, SQLModel
from typing import Optional

# --- Model 1: Equipment (Ekipman) ---
class Equipment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cihaz_turu: str
    marka_model: str
    zimmetli_personel: str
    durum: str = Field(default="Depoda")

# --- Model 2: Ticket (Arıza Kaydı) ---
class Ticket(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    bildiren: str
    aciklama: str
    durum: str = Field(default="Açık")
    cihaz_id: int = Field(foreign_key="equipment.id")