from sqlalchemy.ext.declarative import declarative_base, as_declarative, declared_attr

Base = declarative_base()


@as_declarative()
class Base:
  __name__: str

  # Generate __tablename__ automatically
  @declared_attr
  def __tablename__(cls) -> str:
    return cls.__name__.lower()
