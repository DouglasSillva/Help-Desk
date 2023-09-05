from sqlalchemy import Column, create_engine
from sqlalchemy import Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase, relationship

engine = create_engine("sqlite:///homolog.db", echo=True)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=100), name='nome', nullable=False)
    lastname = Column(String(length=100), name='sobrenome', nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r})"


class Reports(Base):
    __tablename__ = 'chamados'

    id = Column(Integer, primary_key=True)
    subject = Column(String(length=80), name='assunto', nullable=False)
    report = Column(String(length=100), name='chamado', nullable=False)
    pending = Column(Boolean, default=True, name='pendente', nullable=False)
    finished = Column(Boolean, default=False, name='concluido', nullable=False)
    in_progress = Column(Boolean, default=False,
                         name='em_andamento', nullable=False)

    user_id = Column(Integer, ForeignKey(column='usuarios.id'),
                     name='usuarios_id', nullable=False)

    def __repr__(self):
        return f"Report(id={self.id!r}, subject={self.subject!r})"
