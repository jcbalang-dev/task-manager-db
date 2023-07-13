from sqlalchemy import Column, ForeignKey

from sqlalchemy.dialects.mysql import BIGINT

from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task_tag(Base):
    __tablename__ = 'task_tag'

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    task_id = Column(BIGINT, ForeignKey('task.id', ondelete='CASCADE', onupdate='CASCADE'))
    task = relationship('Task', back_populates='tags')
    tag_id = Column(BIGINT, ForeignKey('tag.id', ondelete='CASCADE', onupdate='CASCADE'))
    tag = relationship('Tag', back_populates='task_tags')

class Tag(Base):
    __tablename__ = 'tag'

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    task_tags = relationship('Task_tag', back_populates='tag')