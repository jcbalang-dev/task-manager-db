from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, TEXT

from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, DATETIME

import sqlalchemy as sa

Base = declarative_base()

class Label(Base):
    __tablename__ = 'label'

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(255))
    created_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)