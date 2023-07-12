from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Enum, Table
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, DATETIME
from sqlalchemy.orm import relationship

import sqlalchemy as sa
from role import Role

Base = declarative_base()

user_role_association = Table(
    'user_role_association',
    Base.metadata,
    Column('user_id', BIGINT, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE')),
    Column('role_id', BIGINT, ForeignKey('role.id', ondelete='CASCADE', onupdate='CASCADE'))
)

class User(Base):
    __tablename__ = 'user'

    id = Column(BIGINT, nullable=False, primary_key=True)
    role_id = Column(BIGINT, ForeignKey('role.id', ondelete='CASCADE', onupdate='CASCADE'))
    role = relationship(Role)
    last_name = Column(VARCHAR(100))
    first_name = Column(VARCHAR(50))
    middle_name = Column(VARCHAR(100))
    username = Column(VARCHAR(100))
    email = Column(VARCHAR(255))
    password = Column(VARCHAR(250))
    contact_number = Column(VARCHAR(20))
    status = Column(Enum('free', 'basic', 'starter', 'premium'))
    created_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = Column(DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)