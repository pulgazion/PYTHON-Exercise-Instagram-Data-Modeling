import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    nombre_usuario = Column(String(30), unique=True, nullable=False)
    correo_electronico = Column(String(100), unique=True, nullable=False)
    imagen_perfil = Column(String(200), nullable=False)
    publicaciones = relationship("Publicacion", back_populates="usuario")
    comentarios = relationship("Comentario", back_populates="usuario")
    seguidores = relationship("Seguidores", back_populates="usuario")
    


class Publicacion(Base):
    __tablename__ = 'publicaciones'

    id = Column(Integer, primary_key=True)
    texto = Column(String(200), nullable=False)
    imagen = Column(String(200), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship("Usuario", back_populates="publicaciones")
    comentarios = relationship("Comentario", back_populates="publicacion")



class Comentario(Base):
    __tablename__ = 'comentarios'

    id = Column(Integer, primary_key=True)
    texto = Column(String(200), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    publicacion_id = Column(Integer, ForeignKey('publicaciones.id'))
    usuario = relationship("Usuario", back_populates="comentarios")
    publicacion = relationship("Publicacion", back_populates="comentarios")


class Seguidores(Base):
    __tablename__ = 'seguidores'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship("Usuario", back_populates="seguidores")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
