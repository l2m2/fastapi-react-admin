from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declared_attr


class IDMixin(object):
  id = Column(Integer, primary_key=True, index=True)


class AuditMixin(object):

  @declared_attr
  def created_at(cls):
    return Column(DateTime, server_default=func.now(), nullable=False)

  @declared_attr
  def created_by(cls):
    return Column(Integer, nullable=True)

  @declared_attr
  def updated_at(cls):
    return Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

  @declared_attr
  def updated_by(cls):
    return Column(Integer, nullable=True)


class SoftDeleteMixin:
  deleted_at = Column(DateTime, nullable=True)

  def soft_delete(self):
    self.deleted_at = func.now()
