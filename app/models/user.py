from sqlalchemy import Column, String, CHAR

from app.models import Base


class TblUsers(Base):
    __tablename__ = 'tbl_users'

    id = Column(String(64), primary_key=True)
    password = Column(CHAR(93))  # len(werkzeug.security.generate_password_hash())
    nickname = Column(String(32))