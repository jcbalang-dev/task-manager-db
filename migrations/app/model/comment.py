from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, TEXT, ForeignKey

from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, DATETIME

from sqlalchemy.orm import relationship

import sqlalchemy as sa

from migrations.app.model import Task, Activity

Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'
    
    id = Column(BIGINT, nullable=False, primary_key=True)
    task_id = relationship("Task", back_populates="task_id", foreign_keys='Task.id')

class Activity(Base):
    __tablename__ = 'activity'
    
    id = Column(BIGINT, nullable=False, primary_key=True)
    activity_id = relationship("Activity", back_populates="activty_id", foreign_keys='Activity.id')

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    task_id = Column(BIGINT, ForeignKey('task.id', ondelete='CASCADE', onupdate='CASCADE'))
    task = relationship(Task)
    activity_id = Column(BIGINT, ForeignKey('activity.id', ondelete='CASCADE', onupdate='CASCADE'))
    activity = relationship(Activity)
    title = Column(VARCHAR(100))
    created_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)
    content = Column(TEXT)