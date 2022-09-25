from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from sqlalchemy import INTEGER, String, Column


engine = create_engine('postgresql://uttam:""@localhost/imap_sync', echo=True)
Base = declarative_base()


class Email(Base):
    __tablename__ = 'email'
    row_id = Column(INTEGER, primary_key=True, autoincrement=True)
    message_uid = Column(INTEGER)
    folder_name = Column(String(255))


Base.metadata.create_all(engine)