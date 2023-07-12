from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, ForeignKey

from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, DATETIME, TEXT

from sqlalchemy.orm import relationship

import sqlalchemy as sa

Base = declarative_base()

class Site(Base):
    __tablename__ = 'site'

    id = Column(BIGINT, nullable=False, primary_key=True)
    site_contact = relationship("Site_contact", uselist=False, back_populates="site")

class Site_contact(Base):
    __tablename__ = 'site_contact'

    id = Column(BIGINT, nullable=False, primary_key=True)
    site_id = Column(BIGINT, ForeignKey('site.id', ondelete='CASCADE', onupdate='CASCADE'), unique=True)
    site = relationship("Site", back_populates="site_contact")
    last_name = Column(VARCHAR(100))
    first_name = Column(VARCHAR(50))
    middle_name = Column(VARCHAR(50))
    email = Column(VARCHAR(255))
    contact_number = Column(VARCHAR(20))
    subject = Column(VARCHAR(100))
    message = Column(TEXT)
    created_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)