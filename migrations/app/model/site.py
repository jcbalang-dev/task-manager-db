from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, TEXT

from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, DATETIME

import sqlalchemy as sa

Base = declarative_base()

class Site(Base):
    __tablename__ = 'site'

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(255), unique=True)
    url = Column(VARCHAR(255), unique=True)
    description = Column(TEXT)
    created_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)