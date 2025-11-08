from sqlmodel import create_engine, Session, SQLModel

# Kurulum gerektirmeyen SQLite veritabanı kullanıyoruz.
sqlite_file_name = "veritabani.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# echo=True ayarı, SQL sorgularını terminalde gösterir (hata ayıklama için)
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    """Veritabanını ve tabloları oluşturur."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Her API isteği için bir veritabanı oturumu (session) açar."""
    with Session(engine) as session:
        yield session