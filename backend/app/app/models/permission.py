from sqlalchemy import Column, String
from sqlalchemy.dialects import postgresql
from app.db.base import Base


class Permission(Base):
  __tablename__ = "auth_permission"

  code = Column(String(255), primary_key=True, index=True)
  conf = Column(postgresql.JSONB)

  def __repr__(self):
    return f"<Permission(Code={self.code})>"
