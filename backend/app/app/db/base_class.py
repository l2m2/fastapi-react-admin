from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# @as_declarative()
# class Base:
#   id: Any
#   __name__: str

#   # Generate __tablename__ automatically
#   @declared_attr
#   def __tablename__(cls) -> str:
#     return cls.__name__.lower()
