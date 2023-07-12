from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, ForeignKey, Enum, TIME

from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, DATETIME, TEXT, BLOB, DATE, INTEGER

from sqlalchemy.orm import relationship

import sqlalchemy as sa

from migrations.app.model import User, Project

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(BIGINT, nullable=False, primary_key=True)
    user_id = relationship("Task", back_populates="user_id", foreign_keys='User.id')
    created_by = relationship("Task", back_populates="created_by_user", foreign_keys='Task.created_by')
    updated_by = relationship("Task", back_populates="updated_by_user", foreign_keys='Task.updated_by')

class Project(Base):
    __tablename__ = 'project'

    id = Column(BIGINT, nullable=False, primary_key=True)
    tasks = relationship("Task", back_populates="project")

class Task(Base):
    __tablename__ = 'task'

    id = Column(BIGINT, nullable=False, primary_key=True)
    user_id = Column(BIGINT, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    user = relationship(User)
    title = Column(VARCHAR(50))
    description = Column(TEXT())
    attachment = Column(BLOB())
    status = Column(Enum('pending', 'in progress', 'completed'))
    hours = Column(TIME())
    project_id = Column(BIGINT, ForeignKey('project.id', ondelete='CASCADE', onupdate='CASCADE'))
    project = relationship(Project)
    assigned_to = Column(VARCHAR(100))
    planned_start_date = Column(DATE())
    planned_end_date = Column(DATE())
    actual_start_date = Column(DATE())
    actual_end_date = Column(DATE())
    due_date = Column(DATE())
    priority = Column(INTEGER())
    status = Column(Enum('free', 'basic', 'starter', 'premium'))
    created_by = Column(BIGINT, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    user = relationship(User)
    updated_by = Column(BIGINT, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    user = relationship(User)
    created_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)