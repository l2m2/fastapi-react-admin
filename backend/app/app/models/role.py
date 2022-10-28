from sqlalchemy import String, Column
from app.db.base_class import Base
from app.mixins.common import IDMixin, AuditMixin


class Role(Base, IDMixin, AuditMixin):
  __tablename__ = "auth_role"

  name = Column(String(20), unique=True, index=True, nullable=False)
  description = Column(String)

  def __repr__(self):
    return f"<Role(name={self.name})>"
