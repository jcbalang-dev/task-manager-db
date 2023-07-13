from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, ForeignKey, Enum, TIME

from sqlalchemy.dialects.mysql import BIGINT, DATETIME, TEXT, DATE, INTEGER

from sqlalchemy.orm import relationship

import sqlalchemy as sa

from migrations.app.model import User, Project, Task

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(BIGINT, nullable=False, primary_key=True)
    user_id = relationship("Activity", back_populates="user_id", foreign_keys='User.id')
    assigned_to = relationship("Activity", back_populates="user_id", foreign_keys='User.id')

class Task(Base):
    __tablename__ = 'task'

    id = Column(BIGINT, nullable=False, primary_key=True)    
    task_id = relationship("Activity", back_populates="task_id", foreign_keys='Task.id')

class Project(Base):
    __tablename__ = 'project'

    id = Column(BIGINT, nullable=False, primary_key=True)
    tasks = relationship("Activity", back_populates="project")

class Task(Base):
    __tablename__ = 'task'

    id = Column(BIGINT, nullable=False, primary_key=True)
    user_id = Column(BIGINT, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    user = relationship(User)
    task_id = Column(BIGINT, ForeignKey('task.id', ondelete='CASCADE', onupdate='CASCADE'))
    task = relationship(Task)
    description = Column(TEXT())
    status = Column(Enum('pending', 'in progress', 'completed'))
    hours = Column(TIME())
    project_id = Column(BIGINT, ForeignKey('project.id', ondelete='CASCADE', onupdate='CASCADE'))
    project = relationship(Project)
    assigned_to = Column(BIGINT, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    assigned_to = relationship(User)
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