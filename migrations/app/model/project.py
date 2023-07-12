from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, ForeignKey

from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, TEXT, DATETIME

from sqlalchemy.orm import relationship

import sqlalchemy as sa

from migrations.app.model import Site, User

Base = declarative_base()

class Site(Base):
    __tablename__ = 'site'

    id = Column(BIGINT, nullable=False, primary_key=True)
    site = relationship("Site", uselist=False, back_populates="site")

class User(Base):
    __tablename__ = 'user'

    id = Column(BIGINT, nullable=False, primary_key=True)
    created_by = relationship("Project", back_populates="created_by_user", foreign_keys='Project.created_by')
    updated_by = relationship("Project", back_populates="updated_by_user", foreign_keys='Project.updated_by')

class Project(Base):
    __tablename__ = 'project'

    id = Column(BIGINT, nullable=False, primary_key=True)
    name = Column(VARCHAR(100), unique=True)
    site_id = Column(BIGINT, ForeignKey('site.id', ondelete='CASCADE', onupdate='CASCADE'))
    site = relationship(Site)
    description = Column(TEXT)
    created_by = Column(BIGINT, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    user = relationship(User)
    updated_by = Column(BIGINT, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    user = relationship(User)
    created_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)