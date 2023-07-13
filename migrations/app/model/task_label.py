from sqlalchemy import Column, ForeignKey

from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, DATETIME

import sqlalchemy as sa

from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Label(Base):
    __tablename__ = 'label'

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    task_labels = relationship('Task_label', back_populates='label')

class Task_label(Base):
    __tablename__ = 'task_label'

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    label_id = Column(BIGINT, ForeignKey('label.id', ondelete='CASCADE', onupdate='CASCADE'))
    label = relationship('Label', back_populates='task_labels')
    name = Column(VARCHAR(255), unique=True)
    created_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)