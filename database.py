"""Conexion con la base de datos SQLite mediante SQLAlchemy."""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# El fichero tienda.db se crea en la carpeta desde la que se arranca el servidor
SQLALCHEMY_DATABASE_URL = "sqlite:///./tienda.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
