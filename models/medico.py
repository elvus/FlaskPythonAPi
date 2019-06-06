import uuid
from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'hangvirus'


class Medico(Base):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    nombre_doc = columns.Text()
    cin = columns.Text()
    horario = columns.Text()
    estado_doc = columns.Text()
    especialidad = columns.Text()

    def get_data(self):
        return {
            'id': str(self.id),
            'nombre': self.nombre_doc,
            'cin': self.cin,
            'horario': self.horario,
            'estado': self.estado_doc,
            'especialidad': self.especialidad
        }