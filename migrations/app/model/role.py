from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, TEXT

from sqlalchemy.dialects.mysql import BIGINT, VARCHAR

Base = declarative_base()

class Role(Base):
    __tablename__ = 'role'

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    title = Column(VARCHAR(255), unique=True)
    slug = Column(VARCHAR(255))
    description = Column(TEXT)