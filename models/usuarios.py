import uuid
from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'hangvirus'


class Usuarios(Base):
    id = columns.Integer(primary_key=True)
    nombre = columns.Text()
    password = columns.Text()
    estado = columns.Boolean()

    def get_data(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'password': self.password,
            'estado': self.estado
        }