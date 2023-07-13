from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column

from sqlalchemy.dialects.mysql import BIGINT, VARCHAR

Base = declarative_base()

class Tag(Base):
    __tablename__ = 'tag'

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    title = Column(VARCHAR(255))
    slug = Column(VARCHAR(255))