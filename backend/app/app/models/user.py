from sqlalchemy import Boolean, Column, String
from app.db.base_class import Base
from app.mixins.common import IDMixin, AuditMixin


class User(Base, IDMixin, AuditMixin):
  __tablename__ = "auth_user"

  username = Column(String(20), unique=True, index=True, nullable=False)
  fullname = Column(String(20))
  email = Column(String)
  password = Column(String, nullable=False)
  is_active = Column(Boolean(), default=True)
  is_superuser = Column(Boolean(), default=False)

  def __repr__(self):
    return f"<User(username = {self.username}, fullname = {self.fullname})>"
