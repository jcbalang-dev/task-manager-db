from sqlalchemy import Column, ForeignKey

from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, TEXT

Base = declarative_base()

class TaskMeta(Base):
    __tablename__ = 'task_meta'

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    task_id = Column(BIGINT, ForeignKey('task.id', ondelete='CASCADE', onupdate='CASCADE'))
    meta_key = Column(VARCHAR(255))
    content = Column(TEXT)
    task = relationship('Task', back_populates='meta')

class Task(Base):
    __tablename__ = 'task'

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    meta = relationship('TaskMeta', back_populates='task')